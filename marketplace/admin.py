from django.contrib import admin
from .models import Product, ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'author_id')  # Используем 'id' вместо 'title'
    search_fields = ('name', 'description', 'image', 'author_id',)  # Ищем только по 'text'
    list_filter = ('author_id', 'created_at')

class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)