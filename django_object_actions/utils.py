from django.conf.urls.defaults import patterns
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin


class DjObjectTools(object):
    """
    mixin to add object-tools just like you would add admin actions.

    Tools are defined just like defining actions as modeladmin methods, see:
    https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/#actions-as-modeladmin-methods
    and follow this prototype:

        def toolfunc(self, request, obj)

    They are exposed by putting them in a djobjecttools attribute in your
    modeladmin like:

        class MyModelAdmin(DjObjectTools, admin.ModelAdmin):
            def toolfunc(self, request, obj):
                pass
            toolfunc.short_description = "does nothing"

            djobjecttools = ('toolfunc',)

    Why this functionality isn't baked into contrib.admin is beyond me.

    TODO: get `form` and `change` so you can write tools that can also save
    TODO: handle getting returned an HttpResponse
    """
    change_form_template = "djobjecttools/change_form.html"

    def get_tool_urls(self):
        tools = {}
        for tool in self.djobjecttools:
            tools[tool] = getattr(self, tool)
        my_urls = patterns('',
            (r'^(?P<pk>\d+)/tools/(?P<tool>\w+)/$', self.admin_site.admin_view(
                ModelToolsView.as_view(model=self.model, tools=tools)))
        )
        return my_urls

    def get_urls(self):
        urls = super(DjObjectTools, self).get_urls()
        return self.get_tool_urls() + urls

    def render_change_form(self, request, context, **kwargs):
        context['djtools'] = [(x,
            getattr(getattr(self, x), 'short_description', ''))
            for x in self.djobjecttools]
        return super(DjObjectTools, self).render_change_form(request,
            context, **kwargs)


class ModelToolsView(SingleObjectMixin, View):
    tools = {}

    def get(self, request, **kwargs):
        obj = self.get_object()
        try:
            self.tools[kwargs['tool']](request, obj)
        except KeyError:
            raise Http404
        back = request.path.rsplit('/', 3)[0] + '/'
        return HttpResponseRedirect(back)

    def message_user(self, request, message):
        # copied from django.contrib.admin.options
        messages.info(request, message)
