from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from .models import Article
# Create your views here.

def basic_one(request):
    view = ["basic_one"]
    return render_to_response('myview.html', {'name': view})

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

