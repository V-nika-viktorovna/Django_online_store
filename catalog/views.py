from django.http import HttpResponse
from django.shortcuts import render


def home_view(request):
    """Контроллер для GET запроса при переходе на страницу home"""

    return render(request, 'home.html')


def contacts_view(request):
    """Контроллер для выполнения GET запроса при переходе на страницу contacts,
    и выполнения POST запроса при отправке данных из формы 'Свяжитесь с нами' """

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get("phone")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.\
                            Мы связемся с вами по номеру телефона {phone}")

    return render(request, 'contacts.html')
