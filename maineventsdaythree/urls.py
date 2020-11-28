from django.urls import path
from . import views
app_name="maineventsdaythree"
urlpatterns=[
    path("", views.index, name="index"),
    path("maineventsdaythree", views.maineventsdaythree, name="maineventsdaythree")
]