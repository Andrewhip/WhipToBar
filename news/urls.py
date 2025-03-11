from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='news_home'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),# Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)