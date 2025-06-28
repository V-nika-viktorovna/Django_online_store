from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    """Шаблонный фильтр
    Добавляет к пути папку media"""

    if path:

        path = f'/media/{path}'

        return path
    return '#'
