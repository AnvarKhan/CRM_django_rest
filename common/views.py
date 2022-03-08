from django.shortcuts import render

from django.views.generic import TemplateView, CreateView

from .models import Product

from .forms import SignUpForms

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin




class HomeView(TemplateView):
    template_name = 'common/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = SignUpForms
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'
