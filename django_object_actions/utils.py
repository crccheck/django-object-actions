from functools import wraps

from django.conf.urls import url
from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin

import types


class DjangoObjectActions(object):
    """ModelAdmin mixin to add object-tools just like adding admin actions."""

    # override default change_list_template
    change_list_template = "django_object_actions/change_list.html"
    # override default change_form_template
    change_form_template = "django_object_actions/change_form.html"
    # list to hold each object action tool
    objectactions = []
    # list to hold each model action tool
    modelactions = []

    def get_tool_urls(self):
        """Gets the url patterns that route each tool to a special view."""

        tools = {}
	#Both objectactions and modelactions should be a list type (like in admin actions)
	#Some people (and tox test units) use type instead, so to keep backward copatybility 
	#I cast them to list.
        for tool in list(self.objectactions) + list(self.modelactions):
	    #TODO - check if this is enought to have tools splited over different instances
	    # in case where DjangoObjectActions mixin is used with few ModelAdmin subclasses.
	    if hasattr(self, tool):
                tools[tool] = getattr(self, tool)

        my_urls = []
        if self.objectactions:
            my_urls.append(url(r'^(?P<pk>\d+)/tools/(?P<tool>\w+)/$', 
            self.admin_site.admin_view(ObjectToolsView.as_view(model=self.model, tools=tools))))

        if self.modelactions:
            my_urls.append(url(r'tools/(?P<tool>\w+)/$',
	    self.admin_site.admin_view(ModelToolsView.as_view(model=self.model, tools=tools))))
	    
        return my_urls

    def get_urls(self):
        """Prepends `get_urls` with our own patterns."""

        urls = super(DjangoObjectActions, self).get_urls()
        return self.get_tool_urls() + urls

    def get_tools_context(self, tool_list):
        """Return list that represents the tools func as a dict with extra meta."""

	ret = []
        for tool_name in tool_list:
	    # TODO - The same issue with get_tool_urls - make sure that this enought.
	    if hasattr(self, tool_name):
                tool = getattr(self, tool_name)
                ret.append(dict(name = tool_name,
                                label=getattr(tool, 'label', tool_name.replace('_', ' ')),
                                short_description=getattr(tool, 'short_description', tool.__doc__ or '')))
        return ret

    def render_change_form(self, request, context, **kwargs):
        """Puts `objectactions` into the context."""

        if self.objectactions:
            context['objectactions'] = self.get_tools_context(self.objectactions)

        return super(DjangoObjectActions, self).render_change_form(request,
            context, **kwargs)

    def changelist_view(self, request, extra_context={}):
        """Puts `modelactions` into the context."""

        if self.modelactions:
            extra_context['modelactions'] = self.get_tools_context(self.modelactions)

        return super(DjangoObjectActions, self).changelist_view(request, extra_context)


class ModelToolsView(View):
    """A special view that run the tool's callable, and pass model(class) to it."""

    tools = {}
    model = None

    def get_object(self):
        # Return model itself instead object instance.
        # This method will be override by SingleObjectMixin in ObjectToolsView.
        # By this way we can play with model(class) and model instance (object).
        return self.model

    def get(self, request, **kwargs):
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


class ObjectToolsView(SingleObjectMixin, ModelToolsView):
    """A special view that run the tool's callable, and pass object instance to it."""

    # Subclasssing from SingleObjectMixin set all things.
    # SingleOjectMixin's `get_object`. Works because the view
    #   is instantiated with `model` and the urlpattern has `pk`.
    pass


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


def with_prefixed_action(cls):
    """Class decorator that allow use prefixes for action methods.
       It can be used to fill proper 'actions', 'modelactions', 'objectactions' lists.
       If short_description is None then __doc__ is used instead.
       For label (if empty) the function name is used without prefix and '_' replaced by empty space.
    """
    p = [('acts_', 'actions'), ('actm_', 'modelactions'), ('acto_', 'objectactions')]
    # Allow override prefixes by class 'action_prefixes' list.
    p = getattr(cls, 'action_prefixes', p)
    for name, func in vars(cls).items():
        if isinstance(func, types.FunctionType):
            for prefix, attr in p:
                if name.startswith(prefix):
                    func.short_description = getattr(func, 'short_description', func.__doc__ or '')
                    func.label = getattr(func, 'label', name.partition(prefix)[2].replace('_',' '))
                    getattr(cls, attr, []).append(name)
    return cls
