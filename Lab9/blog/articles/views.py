# articles/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def archive(request):
    posts = Article.objects.all()  # ← archive.html
    print(f"Найдено статей: {posts.count()}")  # Для отладки
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    #print(f"\n[DEBUG] BASE_DIR: {settings.BASE_DIR}")
    #print(f"[DEBUG] APP_DIRS: {settings.TEMPLATES[0]['APP_DIRS']}")
    #print(f"[DEBUG] INSTALLED_APPS: {settings.INSTALLED_APPS}\n")
    post = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article.html', {"post": post})


@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        text = request.POST.get("text", "").strip()

        if not title or not text:
            return render(request, 'articles/create_post.html', {
                'form': {
                    'errors': "Не все поля заполнены",
                    'title': title,
                    'text': text
                }
            })

        if Article.objects.filter(title=title).exists():
            return render(request, 'articles/create_post.html', {
                'form': {
                    'errors': "Статья с таким названием уже существует",
                    'title': title,
                    'text': text
                }
            })

        article = Article.objects.create(
            title=title,
            text=text,
            author=request.user
        )

        return redirect('articles:get_article', article_id=article.id)

    return render(request, 'articles/create_post.html', {})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password2 = request.POST.get('password2', '').strip()

        if not all([username, email, password, password2]):
            return render(request, 'articles/register.html', {
                'error': 'Все поля обязательны для заполнения'
            })

        if password != password2:
            return render(request, 'articles/register.html', {
                'error': 'Пароли не совпадают'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'articles/register.html', {
                'error': 'Пользователь с таким именем уже существует'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('articles:archive')

    return render(request, 'articles/register.html', {})


def auth_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not password:
            return render(request, 'articles/login.html', {
                'error': 'Введите логин и пароль'
            })

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('articles:archive')
        else:
            return render(request, 'articles/login.html', {
                'error': 'Неверный логин или пароль'
            })

    if request.user.is_authenticated:
        return redirect('articles:archive')

    return render(request, 'articles/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('articles:archive')