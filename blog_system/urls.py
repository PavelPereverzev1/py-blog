from django.contrib import admin
from django.urls import path, include
from setuptools import namespaces

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "blog/",
        include("blog.urls", namespace="blog"),
    ),
]
