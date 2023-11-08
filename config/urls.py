from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("management/", admin.site.urls),
    path("blog/", include("blog.urls")),
]
