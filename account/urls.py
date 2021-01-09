from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.main, name="main"),
    path("search", views.search, name="search"),
    path("add", views.add, name="add"),
    path("remove", views.remove, name="remove"),
    path("later", views.later, name="later"),
    path("next", views.next, name="next")
]