from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render

from . import forms


class TopView(TemplateView):
    template_name = "accounts/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "accounts/login.html"

