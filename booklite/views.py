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
    published = data['published']
    publisher = data['publisher']
    img_url = data['cover_url']
    description = data['description']
    pagecount = data['pagecount']
    isbn = data['isbn']
    if Book.objects.filter(isbn=isbn).exists():
        book = Book.objects.get(isbn=isbn)
    else:
        book = Book(title=title, author=author, description=description, publisher=publisher, published=published, img_url=img_url, pagecount=pagecount, isbn=isbn)
        book.save()    
    book.users.add(request.user)
    book.save()

    # print(title)
    return HttpResponse('Book successfully saved')

def registration(request):
    return render(request, 'booklite/registration.html', {})

def register_user(request):     
    username = request.POST['username']    
    password = request.POST['password']
    confirm_password = request.POST('confirm_password')
    if password != confirm_password:
        return HttpResponseRedirect(reverse('booklite:registration'))
    user = User.objects.create_user(username, password)
    login(request, user)
    
    return HttpResponseRedirect(reverse('booklite:index'))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('booklite:index'))
    return HttpResponseRedirect(reverse('booklite:registration'))

    

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('booklite:index'))

def my_books(request):
    # books = {'books': []}
    # for book in request.user.books.all():
    #     books['books'].append({
    #         'title': book.title,
    #         'author': book.author,
    #         'description': book.description,
    #         'img_url': book.img_url,
    #         'publisher': book.publisher,
    #         'published': book.published,
    #         'isbn': book.isbn,
    #         'pagecount': book.pagecount
    #     })
    # return JsonResponse(books)
    books = request.user.books.all()
    return render(request, 'booklite/my_books.html', {'books': books})


def view_my_books(request):
    return HttpResponseRedirect(reverse('booklite:my_books'))
# def view_my_books(request):
    


