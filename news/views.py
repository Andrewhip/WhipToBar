<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import CommentForm
from django.core.cache import cache


class PostListView(ListView):
    model = Post
    template_name = 'news/index.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        cache_key = "post_list"
        posts = cache.get(cache_key)

        if not posts:
            posts = Post.objects.all().order_by('-published_at')
            cache.set(cache_key, posts, 60)  # Кешируем на 1 минуту

        return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)  # Вывод контекста в консоль для отладки
        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        # Кешируем комментарии на 1 минуту
        cache_key = f"comments_{self.object.pk}"
        comments = cache.get(cache_key)
        if not comments:
            comments = self.object.comments.all()
            cache.set(cache_key, comments, 60)

        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            # Обновляем кеш после добавления нового комментария
            cache_key = f"comments_{post.pk}"
            cache.delete(cache_key)

        return redirect('news_detail', pk=post.pk)

=======
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
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832


def about(request):
    return render(request, 'news/about.html')
<<<<<<< HEAD

def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500(request):
    return render(request, 'errors/500.html', status=500)

def custom_403(request, exception):
    return render(request, 'errors/403.html', status=403)

def custom_400(request, exception):
    return render(request, 'errors/400.html', status=400)
=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
