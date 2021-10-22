from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy

class HomeSocioproductivo(LoginRequiredMixin, generic.TemplateView):
    template_name = 'app/HomeSocioproductivo.html'
    login_url = 'app:login'
