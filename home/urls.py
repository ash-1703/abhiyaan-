from django.urls import path
from . import views
app_name="home"
urlpatterns=[
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("about", views.about, name="about")
]