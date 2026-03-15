
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    path('article/new/', views.create_post, name='create_post'),

    path('login/', views.auth_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]