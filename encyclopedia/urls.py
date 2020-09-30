from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entries>", views.viewpage, name="viewpage"),
    path("random", views.rand, name="rand"),
    path("search", views.search, name = "search"),
    path("createPage", views.createPage, name = "createPage"),
    path("editPage/<str:title>", views.editPage, name="editPage")
]
