from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve
try:
    from django.conf.urls import patterns
except ImportError:
    # DJANGO1.6 DJANGO1.7
    # https://docs.djangoproject.com/en/1.8/releases/1.8/#django-conf-urls-patterns
    def patterns(__, *urlpatterns):
        return urlpatterns

from example_project.polls.admin import support_admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^support/', include(support_admin.urls)),
    # serve media
    url(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
)
