# articles/urls.py
from django.urls import path
from . import views

#app_name = 'articles'  # ← пространство имён для url

urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('article/new/', views.create_post, name='create_post'),
]