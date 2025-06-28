from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from catalog.forms import ProductCreateForms

from .models import Product


class CatalogListViev(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class CatalogContactsViev(View):

    def get(self, request):
        return render(request, 'contacts.html')

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get("phone")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.\
                                    Мы связемся с вами по номеру телефона {phone}")


class CatalogCreateView(CreateView):
    model = Product
    form_class = ProductCreateForms
    template_name = 'product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')


class CatalogUpdateView(UpdateView):
    model = Product
    form_class = ProductCreateForms
    template_name = 'product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')


class CatalogDetailViev(DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'products'


class CatalogDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
