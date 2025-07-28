from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def list_products_in_category(category):
    """Функция получает весь список товаров в категории"""

    list_products = Product.objects.filter(category=category)

    result_list = []
    for product in list_products:
        result_list.append(product.name)

    result = ", ".join(result_list)
    return result


def get_catalog_cache():
    """Функция получает данные из кэша.
     Если кэш пуст, то кэширует данные главной стпаницы"""

    if not CACHE_ENABLED:
        return Product.objects.all()

    products_get = cache.get("products_list")
    if products_get is not None:
        return products_get

    products_set = Product.objects.all()
    cache.set("product_list", products_set)
    return products_set
