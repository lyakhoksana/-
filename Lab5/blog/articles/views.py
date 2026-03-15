# articles/views.py
from django.shortcuts import render, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
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


@login_required
def create_post(request):
    if request.method == "POST":
        # Получаем данные из формы
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()

        # Проверка: поля не пустые
        if not title or not text:
            return render(request, 'create_post.html', {
                'form': {
                    'errors': "Не все поля заполнены",
                    'title': title,
                    'text': text
                }
            })

        if Article.objects.filter(title=title).exists():
            return render(request, 'create_post.html', {
                'form': {
                    'errors': "Статья с таким названием уже существует",
                    'title': title,
                    'text': text
                }
            })

        # Создаём новую статью
        article = Article.objects.create(
            title=title,
            text=text,
            author=request.user  # Автор = текущий пользователь
        )

        # Перенаправляем на страницу созданной статьи
        return redirect('get_article', article_id=article.id)

    # Если метод GET — просто показываем пустую форму
    return render(request, 'create_post.html', {})
