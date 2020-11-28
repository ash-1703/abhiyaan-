from django.urls import path
from . import views
app_name="maineventsdaytwo"
urlpatterns=[
    path("", views.index, name="index"),
    path("maineventsdaytwo", views.maineventsdaytwo, name="maineventsdaytwo")
]