# Было: from django.http import HttpResponse
#        return HttpResponse(u'Привет, Мир!', mimetype="text/plain")

# Стало:
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # mimetype → content_type
    return HttpResponse('Привет, Мир!', content_type="text/plain")

def home_html(request):
    return render(request, 'index.html', {})