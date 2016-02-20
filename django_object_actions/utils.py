from __future__ import unicode_literals

from functools import wraps
from itertools import chain

from django.conf.urls import url
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponseRedirect
from django.http.response import HttpResponseBase
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class BaseDjangoObjectActions(object):
    """
    ModelAdmin mixin to add object-tools just like adding admin actions.

    Attributes
    ----------
    model : django.db.models.Model
        The Django Model these tools work on. This is populated by Django.
    objectactions : list of str
        Write the names of the callable attributes (methods) of the model admin
        that can be used as tools in the change view.
    changelist_actions : list of str
        Write the names of the callable attributes (methods) of the model admin
        that can be used as tools in the changelist view.
    tools_view_name : str
        The name of the Django Object Actions admin view, including the 'admin'
        namespace. Populated by `get_tool_urls`.
    """
    objectactions = []
    changelist_actions = []
    tools_view_name = None

    def get_tool_urls(self):
        """Get the url patterns that route each tool to a special view."""
        tools = {}

        # Look for the default change view url and use that as a template
        try:
            model_name = self.model._meta.model_name
        except AttributeError:
            # DJANGO15
            model_name = self.model._meta.module_name
        base_url_name = '%s_%s' % (self.model._meta.app_label, model_name)
        model_tools_url_name = '%s_tools' % base_url_name
        change_view_url_name = 'admin:%s_change' % base_url_name

        self.tools_view_name = 'admin:' + model_tools_url_name

        for tool in chain(self.objectactions, self.changelist_actions):
            tools[tool] = getattr(self, tool)
        return [
            # change, supports pks that are numbers or uuids
            url(r'^(?P<pk>[0-9a-f\-]+)/tools/(?P<tool>\w+)/$',
                self.admin_site.admin_view(  # checks permissions
                    ModelToolsView.as_view(
                        model=self.model,
                        tools=tools,
                        back=change_view_url_name,
                    )
                ),
                name=model_tools_url_name),
            # changelist
            url(r'^tools/(?P<tool>\w+)/$',
                self.admin_site.admin_view(  # checks permissions
                    ModelToolsView.as_view(
                        model=self.model,
                        tools=tools,
                        back=change_view_url_name,
                    )
                ),
                name=model_tools_url_name),  # FIXME
        ]

    # EXISTING ADMIN METHODS MODIFIED
    #################################

    def get_urls(self):
        """Prepend `get_urls` with our own patterns."""
        urls = super(BaseDjangoObjectActions, self).get_urls()
        return self.get_tool_urls() + urls

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """Add `objectactions` into the change context."""
        def to_dict(tool_name):
            """To represents the tool func as a dict with extra meta."""
            tool = getattr(self, tool_name)
            standard_attrs, custom_attrs = self.get_djoa_button_attrs(tool)
            return dict(
                name=tool_name,
                label=getattr(tool, 'label', tool_name),
                standard_attrs=standard_attrs,
                custom_attrs=custom_attrs,
            )

        extra_context = {
            'objectactions': [
                to_dict(action) for action in
                self.get_object_actions(request, object_id, form_url)
            ],
            'tools_view_name': self.tools_view_name,
        }
        return super(BaseDjangoObjectActions, self).change_view(
            request, object_id, form_url, extra_context)

    def changelist_view(self, request, extra_context=None):
        """Put `objectactions` into the changelist context."""
        # FIXME DRY
        def to_dict(tool_name):
            """To represents the tool func as a dict with extra meta."""
            tool = getattr(self, tool_name)
            standard_attrs, custom_attrs = self.get_djoa_button_attrs(tool)
            return dict(
                name=tool_name,
                label=getattr(tool, 'label', tool_name),
                standard_attrs=standard_attrs,
                custom_attrs=custom_attrs,
            )

        extra_context = {
            'objectactions': [
                to_dict(action) for action in
                self.get_changelist_actions(request)
            ],
            'tools_view_name': self.tools_view_name,
        }
        return super(BaseDjangoObjectActions, self).changelist_view(
            request, extra_context)

    # CUSTOM METHODS
    ################

    def get_object_actions(self, request, object_id, form_url):
        """
        Override this to customize what actions get to the change view.

        This takes the same parameters as `change_view`.

        For example, to restrict actions to superusers, you could do:

            class ChoiceAdmin(DjangoObjectActions, admin.ModelAdmin):
                def get_object_actions(self, request, **kwargs):
                    if request.user.is_superuser:
                        return super(ChoiceAdmin, self).get_object_actions(
                            request, **kwargs
                        )
                    return []
        """
        return self.objectactions

    def get_changelist_actions(self, request):
        """
        Override this to customize what actions get to the changelist view.
        """
        return self.changelist_actions

    def get_djoa_button_attrs(self, tool):
        """
        Get the HTML attributes associated with a tool.

        There are some standard attributes (class and title) that the template
        will always want. Any number of additional attributes can be specified
        and passed on. This is kinda awkward and due for a refactor for
        readability.
        """
        attrs = getattr(tool, 'attrs', {})
        # href is not allowed to be set. should an exception be raised instead?
        if 'href' in attrs:
            attrs.pop('href')
        # title is not allowed to be set. should an exception be raised instead?
        # `short_description` should be set instead to parallel django admin
        # actions
        if 'title' in attrs:
            attrs.pop('title')
        default_attrs = {
            'class': attrs.get('class', ''),
            'title': getattr(tool, 'short_description', ''),
        }
        standard_attrs = {}
        custom_attrs = {}
        for k, v in dict(default_attrs, **attrs).items():
            if k in default_attrs:
                standard_attrs[k] = v
            else:
                custom_attrs[k] = v
        return standard_attrs, custom_attrs


class DjangoObjectActions(BaseDjangoObjectActions):
    change_form_template = "django_object_actions/change_form.html"
    change_list_template = "django_object_actions/change_list.html"


class ModelToolsView(SingleObjectMixin, View):
    """
    The view that runs the tool's callable.

    Attributes
    ----------
    back : str
        The urlpattern name to send users back to. Defaults to the change view.
    model : django.db.model.Model
        The model this tool operates on.
    tools : dict
        A mapping of tool names to tool callables.
    """
    back = None
    model = None
    tools = None

    def get(self, request, **kwargs):
        # SingleOjectMixin's `get_object`. Works because the view
        #   is instantiated with `model` and the urlpattern has `pk`.
        obj = self.get_object()
        try:
            tool = self.tools[kwargs['tool']]
        except KeyError:
            raise Http404(u'Tool does not exist')

        ret = tool(request, obj)
        if isinstance(ret, HttpResponseBase):
            return ret

        back = reverse(self.back, args=(kwargs['pk'],))
        return HttpResponseRedirect(back)

    # HACK to allow POST requests too easily
    post = get

    def message_user(self, request, message):
        """
        Mimic Django admin actions's `message_user`.

        Like the second example:
        https://docs.djangoproject.com/en/1.9/ref/contrib/admin/actions/#custom-admin-action
        """
        messages.info(request, message)


def takes_instance_or_queryset(func):
    """Decorator that makes standard Django admin actions compatible."""
    @wraps(func)
    def decorated_function(self, request, queryset):
        # func follows the prototype documented at:
        # https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#writing-action-functions
        if not isinstance(queryset, QuerySet):
            try:
                # Django >=1.8
                queryset = self.get_queryset(request).filter(pk=queryset.pk)
            except AttributeError:
                try:
                    # Django >=1.6,<1.8
                    model = queryset._meta.model
                except AttributeError:
                    # Django <1.6
                    model = queryset._meta.concrete_model
                queryset = model.objects.filter(pk=queryset.pk)
        return func(self, request, queryset)
    return decorated_function
