from django.db import models


class Article(models.Model):

    name = models.CharField(max_length=254, verbose_name='Заголовок')
    description = models.TextField(null=True, blank=True, verbose_name='Содержимое')
    image = models.ImageField(null=True, blank=True, upload_to='article/photo', verbose_name='Иллюстрация статьи')
    publication_attribute = models.BooleanField(verbose_name='Признак публикации')
    views = models.PositiveIntegerField(max_length=254, default=0, verbose_name='Количество просмотров')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['name']
