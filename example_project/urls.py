from django import VERSION
from django.conf.urls import url
from django.contrib import admin
from example_project.polls.admin import support_admin

if VERSION[0] == 1 and VERSION[1] <= 8:
    from django.conf.urls import include
else:
    # DJANGO1.9
    # https://docs.djangoproject.com/en/2.0/releases/1.9/#passing-a-3-tuple-or-an-app-name-to-include
    def include(urls):
        return urls


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^support/', include(support_admin.urls)),
]
