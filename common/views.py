from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Product
from .forms import SignUpForms
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'common/home.html'


class SignUpView(CreateView):
    form_class = SignUpForms
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'price')
    template_name = 'product.html'
