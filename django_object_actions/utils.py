from __future__ import unicode_literals

from functools import wraps

from django.conf.urls import url
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class BaseDjangoObjectActions(object):
    """
    ModelAdmin mixin to add object-tools just like adding admin actions.

    Attributes
    ----------
    model : django.db.models.Model
        The Django Model these tools work on. This is populated by Django.
    objectactions : list
        Write the names of the callable attributes (methods) of the model admin
        that can be used as tools.
    tools_view_name : str
        The name of the Django Object Actions admin view. Populated by
        `get_tool_urls`.
    """
    objectactions = []
    tools_view_name = None

    def get_tool_urls(self, urls):
        """Get the url patterns that route each tool to a special view."""
        tools = {}

        # Look for the default change view url and use that as a template
        change_view = None
        end = '_change'
        for url_pattern in urls:
            if url_pattern.name.endswith(end):
                model_tools_url_name = url_pattern.name[:-len(end)] + '_tools'
                change_view = 'admin:' + url_pattern.name
                break
        if not change_view:
            # Should this just replace the above?
            base_url_name = '%s_%s_change' % (
                self.model._meta.app_label,
                self.model._meta.model_name,
            )
            model_tools_url_name = '%s_tools' % base_url_name
            change_view = 'admin:%s' % base_url_name

        self.tools_view_name = 'admin:' + model_tools_url_name

        for tool in self.objectactions:
            tools[tool] = getattr(self, tool)
        my_urls = [
            # supports pks that are numbers or uuids
            url(r'^(?P<pk>[0-9a-f\-]+)/tools/(?P<tool>\w+)/$',
                self.admin_site.admin_view(
                        ModelToolsView.as_view(model=self.model, tools=tools, back=change_view)),
                name=model_tools_url_name)
        ]
        return my_urls

    # EXISTING ADMIN METHODS MODIFIED
    #################################

    def get_urls(self):
        """Prepend `get_urls` with our own patterns."""
        urls = super(BaseDjangoObjectActions, self).get_urls()
        return self.get_tool_urls(urls) + urls

    def render_change_form(self, request, context, **kwargs):
        """Put `objectactions` into the context."""

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

        context['objectactions'] = map(
            to_dict,
            self.get_object_actions(request, context, **kwargs)
        )
        context['tools_view_name'] = self.tools_view_name
        return super(BaseDjangoObjectActions, self).render_change_form(
            request, context, **kwargs)

    # CUSTOM METHODS
    ################

    def get_object_actions(self, request, context, **kwargs):
        """Override this to customize what actions get sent."""
        return self.objectactions

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
        if isinstance(ret, HttpResponse):
            return ret

        back = reverse(self.back, args=(kwargs['pk'],))
        return HttpResponseRedirect(back)

    # HACK to allow POST requests too easily
    post = get

    def message_user(self, request, message):
        """
        Mimic Django admin actions's `message_user`.

        Like the second example:
        https://docs.djangoproject.com/en/1.7/ref/contrib/admin/actions/#custom-admin-action
        """
        # copied from django.contrib.admin.options
        # included to mimic admin actions
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
