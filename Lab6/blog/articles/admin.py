# Было: from models import Article
# Стало:
from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
    list_filter = ('created_date', 'author')
    search_fields = ('title', 'text')