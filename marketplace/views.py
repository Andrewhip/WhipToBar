from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, View
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage
from .forms import ProductForm
from django.urls import reverse

class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/form_by_buy.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()  # Сохраняем продукт

        # Загружаем изображения
        images = self.request.FILES.getlist('images')
        if images:
            for image in images:
                ProductImage.objects.create(product=product, image=image)  # Привязываем изображение к продукту

        return redirect(self.success_url)


class ProductListView(ListView):
    model = Product
    template_name = 'marketplace/product_list.html'  # Шаблон для отображения списка товаров
    context_object_name = 'products'  # Название переменной для товаров в шаблоне

class ProductDetailView(DetailView):
    model = Product
    template_name = 'marketplace/product_detail.html'
    context_object_name = 'product'


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from .models import Product
from .forms import ProductForm


class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'marketplace/product_edit.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        images = self.request.FILES.getlist('images')  # Получаем список файлов
        for image in images:
            ProductImage.objects.create(product=self.object, image=image)
        return response

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