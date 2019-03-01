from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):  
    return render(request, 'booklite/index.html', {})

def save_book(request):
    data = json.loads(request.body)
    print(data)
    title = data['title']
    author = data['author']
    # published = data['published']
    # publisher = data['publisher']
    img_url = data['cover_url']
    # book = Book(title=title, author=author, ..)
    # book.save()
    # print(title)
    return HttpResponse('Book successfully saved')

def registration(request):
    return render(request, 'booklite/registration.html', {})

def register_user(request):     
    username = request.POST['username']    
    password = request.POST['password']
    # confirm_password = request.POST('confirm_password')
    # if password != confirm_password:
    #     return HttpResponseRedirect(reverse('booklite:registration'))
    user = User.objects.create_user(username, password)
    login(request, user)
    
    return HttpResponseRedirect(reverse('booklite:index'))


# def login_user(request):
#     username = request.POST('username')
#     password = request.POST('password')
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)

# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('booklite:index'))

