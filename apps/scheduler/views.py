from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
#後で上のインポートを添削
from . import forms
from django.shortcuts import render


class ScheduleView(LoginRequiredMixin, TemplateView):
    template_name = "scheduler/schedule.html"