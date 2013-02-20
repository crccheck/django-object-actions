from django.conf.urls.defaults import patterns
from django.contrib import messages
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class DjangoObjectActions(object):
    """
    mixin to add object-tools just like you would add admin actions.

    Tools are defined just like defining actions as modeladmin methods, see:
    https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods
    and follow this prototype:

        def toolfunc(self, request, obj)

    They are exposed by putting them in a `objectactions` attribute in your
    modeladmin like:

        class MyModelAdmin(DjangoObjectActions, admin.ModelAdmin):
            def toolfunc(self, request, obj):
                pass
            toolfunc.short_description = "does nothing"

            objectactions = ('toolfunc',)

    Why this functionality isn't baked into contrib.admin is beyond me.

    TODO: get `form` and `change` so you can write tools that can also save
    TODO: handle getting returned an HttpResponse

    """
    # override default change_form_template
    change_form_template = "django_object_actions/change_form.html"
    # list to hold each object action tool
    objectactions = []

    def get_tool_urls(self):
        """ get the url patterns that route each tool to a special view """
        tools = {}
        for tool in self.objectactions:
            tools[tool] = getattr(self, tool)
        my_urls = patterns('',
            (r'^(?P<pk>\d+)/tools/(?P<tool>\w+)/$', self.admin_site.admin_view(
                ModelToolsView.as_view(model=self.model, tools=tools)))
        )
        return my_urls

    def get_urls(self):
        """ prepend `get_urls` with our own patterns """
        urls = super(DjangoObjectActions, self).get_urls()
        return self.get_tool_urls() + urls

    def render_change_form(self, request, context, **kwargs):
        """ put `objectactions` into the context """
        context['objectactions'] = [(x,
            getattr(getattr(self, x), 'short_description', ''))
            for x in self.objectactions]
        return super(DjangoObjectActions, self).render_change_form(request,
            context, **kwargs)


class ModelToolsView(SingleObjectMixin, View):
    """ special view that run the tool's callable """
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
