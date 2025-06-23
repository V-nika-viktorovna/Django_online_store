from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product


def home_view(request):
    """Контроллер для GET запроса при переходе на страницу home"""

    products = Product.objects.all()
    context = {'products': products}

    return render(request, 'home.html', context)


def contacts_view(request):
    """Контроллер для выполнения GET запроса при переходе на страницу contacts,
    и выполнения POST запроса при отправке данных из формы 'Свяжитесь с нами' """

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get("phone")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.\
                            Мы связемся с вами по номеру телефона {phone}")

    return render(request, 'contacts.html')


def product_info_view(request, pk):
    """Контроллер для GET запроса при переходе на страницу product_info"""

    products = get_object_or_404(Product, id=pk)
    context = {'products': products}

    return render(request, 'product_info.html', context)
