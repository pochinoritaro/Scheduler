from django.conf.urls import url
from django.urls import path

from . import views


app_name="scheduler"
urlpatterns = [
    path("", views.ScheduleView.as_view(), name="schedule"),
]