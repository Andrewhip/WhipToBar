from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'published_at', 'source')  # Используем 'id' вместо 'title'
    search_fields = ('text',)  # Ищем только по 'text'
    list_filter = ('source', 'published_at')

admin.site.register(Post, PostAdmin)
