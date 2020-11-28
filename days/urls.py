from django.urls import path
from . import views
app_name="days"
urlpatterns=[
    path("", views.index, name="index"),
    path("<str:day>", views.day, name="day"),
    path("<str:day>/<str:event>", views.event, name="event"),
]