from django.db import models

from users.models import User


class Category(models.Model):

    name = models.CharField(max_length=254, verbose_name='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):

    name = models.CharField(max_length=254, verbose_name='Наименование', help_text='Наименование')
    description = models.TextField(null=True, blank=True, verbose_name='описание', help_text='описание')
    image = models.ImageField(null=True, blank=True, upload_to='product/photo')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория', help_text='категория')
    purchase_price = models.FloatField(default=0, verbose_name='цена за покупку', help_text='цена за покупку')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    publication_status = models.BooleanField(default=False, verbose_name='Признак публикации',
                                             help_text='Признак публикации', null=True, blank=True)
    owner = models.ForeignKey(User, verbose_name='Владелец',
                              help_text='Владелец продукта', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} категория:{self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_products', 'Can delete products')
        ]
