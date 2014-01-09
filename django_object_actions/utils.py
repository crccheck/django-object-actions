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
            return dict(
                name=tool_name,
                label=getattr(tool, 'label', tool_name),
                short_description=getattr(tool, 'short_description', ''))

        context['objectactions'] = [to_dict(x) for x in self.objectactions]
        return super(BaseDjangoObjectActions, self).render_change_form(request,
            context, **kwargs)


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
        super(QuerySetIsh, self).__init__(model, *args, **kwargs)
        self._result_cache = [instance]

    def _clone(self, *args, **kwargs):
        # don't clone me, bro
        return self


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
