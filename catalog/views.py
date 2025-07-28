from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Permission
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from catalog.forms import ProductCreateForms, ProductModeratorForms

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


class CatalogCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreateForms
    template_name = 'product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class CatalogUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductCreateForms
    template_name = 'product_form.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return self.form_class
        if user.has_perm('product.can_unpublish_product'):
            return ProductModeratorForms
        raise PermissionDenied


class CatalogDetailViev(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'products'


class CatalogDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, pk):
        user = self.request.user
        product = self.get_object()
        if user != product.owner and not user.has_perm('product.can_delete_products'):
            return HttpResponseForbidden('У вас недостаточно прав для удаления данного продукта!')
        return self.delete(request, pk)
