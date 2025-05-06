from django.contrib.auth import get_user_model
from django.db import models
<<<<<<< HEAD
from django.urls import reverse

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='products', null=True, default=None, verbose_name='Автор')
    # Это поле не обязательно для продукта, так как изображения будут храниться в ProductImage
    image = models.ImageField(upload_to='marketplace/product_images/', verbose_name='Изображение', null=True, blank=True)

<<<<<<< HEAD
    def get_absolute_url(self):
        # Возвращает URL страницы подробного описания продукта (или другого, соответствующего URL)
        return reverse('product_detail', args=[str(self.id)])

=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
    def __str__(self):
        return self.name

    def get_first_image(self):
        """Возвращает первое изображение товара, если оно есть."""
        return self.images.first()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', verbose_name='Товар')
    image = models.ImageField(upload_to='marketplace/product_images/', verbose_name='Изображение', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Image for {self.product.name}"

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'