
from django.contrib import admin
from django.urls import path
from .apis import api_admin_v1

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_admin/v1/", api_admin_v1.urls),  # <---------- !
]