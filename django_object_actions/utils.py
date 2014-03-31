from functools import wraps

from django.conf.urls import patterns
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class BaseDjangoObjectActions(object):
    """ModelAdmin mixin to add object-tools just like adding admin actions."""
    # list to hold each object action tool
    objectactions = []

    def get_tool_urls(self):
        """Gets the url patterns that route each tool to a special view."""
        tools = {}
        for tool in self.objectactions:
            tools[tool] = getattr(self, tool)
        my_urls = patterns('',
            (r'^(?P<pk>\d+)/tools/(?P<tool>\w+)/$', self.admin_site.admin_view(
                ModelToolsView.as_view(model=self.model, tools=tools)))
        )
        return my_urls

    ###################################
    # EXISTING ADMIN METHODS MODIFIED #
    ###################################

    def get_urls(self):
        """Prepends `get_urls` with our own patterns."""
        urls = super(BaseDjangoObjectActions, self).get_urls()
        return self.get_tool_urls() + urls

    def render_change_form(self, request, context, **kwargs):
        """Puts `objectactions` into the context."""

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

        context['objectactions'] = [
            to_dict(x) for x in
            self.get_object_actions(request, context, **kwargs)
        ]
        return super(BaseDjangoObjectActions, self).render_change_form(
            request, context, **kwargs)

    ##################
    # CUSTOM METHODS #
    ##################

    def get_object_actions(self, request, context, **kwargs):
        return self.objectactions

    def get_djoa_button_attrs(self, tool):
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
    # override default change_form_template
    change_form_template = "django_object_actions/change_form.html"


class ModelToolsView(SingleObjectMixin, View):
    """A special view that run the tool's callable."""
    tools = {}

    def get(self, request, **kwargs):
        # SingleOjectMixin's `get_object`. Works because the view
        #   is instantiated with `model` and the urlpattern has `pk`.
        obj = self.get_object()
        try:
            ret = self.tools[kwargs['tool']](request, obj)
        except KeyError:
            raise Http404
        if isinstance(ret, HttpResponse):
            return ret
        back = request.path.rsplit('/', 3)[0] + '/'
        return HttpResponseRedirect(back)

    # Allow POST
    post = get

    def message_user(self, request, message):
        # copied from django.contrib.admin.options
        # included to mimic admin actions
        messages.info(request, message)


class QuerySetIsh(QuerySet):
    """Takes an instance and mimics it coming from a QuerySet."""
    def __init__(self, instance=None, *args, **kwargs):
        try:
            model = instance._meta.model
        except AttributeError:
            # Django 1.5 does this instead, getting the model may be overkill
            # we may be able to throw away all this logic
            model = instance._meta.concrete_model
        self._doa_instance = instance
        super(QuerySetIsh, self).__init__(model, *args, **kwargs)
        self._result_cache = [instance]

    def _clone(self, *args, **kwargs):
        # don't clone me, bro
        return self

    def get(self, *args, **kwargs):
        # Starting in Django 1.7, `QuerySet.get` started slicing to
        # `MAX_GET_RESULTS`, so to avoid messing with `__getslice__`, override
        # `.get`.
        return self._doa_instance


def takes_instance_or_queryset(func):
    """Decorator that makes standard actions compatible."""
    @wraps(func)
    def decorated_function(self, request, queryset):
        # func follows the prototype documented at:
        # https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#writing-action-functions
        if not isinstance(queryset, QuerySet):
            queryset = QuerySetIsh(queryset)
        return func(self, request, queryset)
    return decorated_function
