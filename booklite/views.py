from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse
from .models import Book
import json

def index(request):  
    return render(request, 'index.html', {})

def save_book(request):
    data = json.loads(request.body)
    title = data['title']
    author = data['author']
    published = data['published']
    publisher = data['publisher']
    img_url = data['cover_url']
    Book.save()
    return HttpResponse('Book successfully saved')
