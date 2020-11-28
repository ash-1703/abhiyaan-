from django.urls import path
from . import views
app_name="maineventsdayone"
urlpatterns=[
    path("", views.index, name="index"),
    path("maineventsdayone", views.maineventsdayone, name="maineventsdayone")
]