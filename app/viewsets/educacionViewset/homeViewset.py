from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/home.html'
    login_url = 'app:login'
