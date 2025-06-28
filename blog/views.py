from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView, View)

from .models import Article


class BlogListView(ListView):
    model = Article

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_attribute=True)


class BlogContactsView(View):

    def get(self, request):
        return render(request, 'blog/contacts_article.html')

    def post(self, request):

        name = request.POST.get('name')
        phone = request.POST.get("phone")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.\
                                    Мы связемся с вами по номеру телефона {phone}")


class BlogDetailView(DetailView):
    model = Article

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogCreateView (CreateView):
    model = Article
    fields = ('name', 'description', 'image', 'publication_attribute')
    success_url = reverse_lazy('blog:home_article')


class BlogUpdateView(UpdateView):
    model = Article
    fields = ('name', 'description', 'image', 'publication_attribute')
    success_url = reverse_lazy('blog:home_article')

    def get_success_url(self):
        return reverse_lazy('blog:article_info', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:home_article')
