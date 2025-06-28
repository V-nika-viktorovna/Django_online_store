from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publication_attribute',)
    list_filter = ('name', 'publication_attribute', 'views', 'created_at', 'updated_at',)
    search_fields = ('name', 'description', 'purchase_price', 'views', 'created_at', 'updated_at',)
