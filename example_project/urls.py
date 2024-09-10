from django.urls import path
from django.contrib import admin
from example_project.polls.admin import support_admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("support/", support_admin.urls),
]
