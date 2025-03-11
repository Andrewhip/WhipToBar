# sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from marketplace.models import Product  # Модель товаров
from news.models import Post  # Модель новостей

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Список URL-адресов статических страниц
        return ['news_home', 'about', 'product_list']  # Имена URL-маршрутов

    def location(self, item):
        return reverse(item)


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Возвращает все объекты модели Post
        return Post.objects.all()

    def lastmod(self, obj):
        # Возвращает дату последнего изменения объекта
        return obj.published_at


class ProductSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        # Возвращает все объекты модели Product
        return Product.objects.all()

    def lastmod(self, obj):
        # Возвращает дату последнего изменения объекта
        return obj.created_at