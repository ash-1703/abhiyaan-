from django.urls import path
from . import views
app_name="sports"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:sport>", views.sport, name="sport")
]