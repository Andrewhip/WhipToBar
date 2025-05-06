from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage
from .forms import ProductForm
from django.urls import reverse

<<<<<<< HEAD

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Product, ProductImage
from .forms import ProductForm


=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/form_by_buy.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
<<<<<<< HEAD
        # Сохраняем продукт
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
=======
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()  # Сохраняем продукт
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

        # Загружаем изображения
        images = self.request.FILES.getlist('images')
        if images:
            for image in images:
<<<<<<< HEAD
                ProductImage.objects.create(product=product, image=image)

        # Возвращаем стандартный ответ
        return super().form_valid(form)



=======
                ProductImage.objects.create(product=product, image=image)  # Привязываем изображение к продукту

        return redirect(self.success_url)
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832


class ProductListView(ListView):
    model = Product
    template_name = 'marketplace/product_list.html'  # Шаблон для отображения списка товаров
    context_object_name = 'products'  # Название переменной для товаров в шаблоне

class ProductDetailView(DetailView):
    model = Product
    template_name = 'marketplace/product_detail.html'
    context_object_name = 'product'


<<<<<<< HEAD

=======
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from .models import Product
from .forms import ProductForm
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_edit.html'

    def form_valid(self, form):
<<<<<<< HEAD
        # Получаем объект продукта
        product = form.save(commit=False)
        product.save()

        # Удаляем выбранные изображения
        delete_images = self.request.POST.getlist('delete_images')
        if delete_images:
            ProductImage.objects.filter(id__in=delete_images).delete()

        # Добавляем новые изображения
        images = self.request.FILES.getlist('images')
        for image in images:
            ProductImage.objects.create(product=product, image=image)

        return super().form_valid(form)
=======
        response = super().form_valid(form)
        images = self.request.FILES.getlist('images')  # Получаем список файлов
        for image in images:
            ProductImage.objects.create(product=self.object, image=image)
        return response
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})



class ProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        # Проверка, если текущий пользователь - автор продукта
        if product.author == request.user:
            product.delete()  # Удаляем продукт
            return redirect('product_list')  # Перенаправляем на список продуктов
        return redirect('product_detail', pk=pk)  # Если автор не совпадает, остаёмся на странице продукта