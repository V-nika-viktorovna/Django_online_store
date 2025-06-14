from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'purchase_price',)
    list_filter = ('name', 'category', 'purchase_price', 'created_at', 'updated_at',)
    search_fields = ('name', 'description', 'category', 'purchase_price', 'created_at', 'updated_at',)
