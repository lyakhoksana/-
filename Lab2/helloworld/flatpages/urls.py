# Было: urlpatterns = patterns('', url(r'^$', 'flatpages.views.home', name='home'))
# Стало:
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_html, name='home'),
    path('hello/', views.home_html, name='hello'),  # Задание: тот же текст по /hello/
]