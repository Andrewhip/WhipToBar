from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'news/index.html'  # Шаблон для главной страницы
    context_object_name = 'posts'  # Название переменной, через которую мы будем обращаться к постам в шаблоне
    paginate_by = 5  # Количество постов на странице

    def get_queryset(self):
        # Получаем все посты и сортируем по дате публикации (по убыванию)
        return Post.objects.all().order_by()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Вывод контекста в консоль
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'  # Укажите ваш шаблон
    context_object_name = 'post'  # Имя объекта в контексте шаблона


def about(request):
    return render(request, 'news/about.html')
