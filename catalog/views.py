from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

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


class CatalogDetailViev(DetailView):
    model = Product
    template_name = 'product_info.html'
    context_object_name = 'products'
