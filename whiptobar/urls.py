"""
URL configuration for whiptobar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.conf.urls import handler404, handler500, handler403, handler400
from django.contrib.sitemaps.views import sitemap
from news.sitemaps import StaticViewSitemap, NewsSitemap, ProductSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'news': NewsSitemap,
    'products': ProductSitemap,
}
=======
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
<<<<<<< HEAD
    path('marketplace/', include('marketplace.urls')),
    path('users/', include('users.urls', namespace="users")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('chat/', include('chat.urls', namespace='chat')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('captcha/', include('captcha.urls')),

]

handler404 = 'news.views.custom_404'
handler500 = 'news.views.custom_500'
handler403 = 'news.views.custom_403'
handler400 = 'news.views.custom_400'

# Добавляем раздачу статики и медиафайлов, если DEBUG включен
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======
    path('marketplace/' , include('marketplace.urls')),
    path('users/' , include('users.urls', namespace="users")),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path("chat/", include("chat.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 7073313818c546dbec1a69bc6d606b01439d6832
