# articles/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.conf import settings

def archive(request):
    posts = Article.objects.all()  # ← archive.html
    print(f"Найдено статей: {posts.count()}")  # Для отладки
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    #print(f"\n[DEBUG] BASE_DIR: {settings.BASE_DIR}")
    #print(f"[DEBUG] APP_DIRS: {settings.TEMPLATES[0]['APP_DIRS']}")
    #print(f"[DEBUG] INSTALLED_APPS: {settings.INSTALLED_APPS}\n")
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'article.html', {"post": post})


