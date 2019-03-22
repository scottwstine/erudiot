from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Book, Genre
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'booklite/index.html', {})


def save_book(request):
    if not request.user.is_authenticated:
        return HttpResponse('not logged in')
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
        book = Book(title=title, author=author, description=description, publisher=publisher,
                    published=published, img_url=img_url, pagecount=pagecount, isbn=isbn)
        book.save()
    book.users.add(request.user)

    genre_names = data['genres']
    for genre_name in genre_names:
        genre, created = Genre.objects.get_or_create(name=genre_name)
        book.genres.add(genre)
    
    return HttpResponse('Book successfully saved')


def registration(request):
    next = request.GET.get('next', '')
    return render(request, 'booklite/registration.html', {'next': next})


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']
    if password != confirm_password:
        return HttpResponseRedirect(reverse('booklite:registration'))
    user = User.objects.create_user(username, password)
    login(request, user)

    return HttpResponseRedirect(reverse('booklite:index'))


def login_user(request):
    print('THIS VIEW IS BEING HIT')
    username = request.POST['username']
    password = request.POST['password']
    next = request.POST['next']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if next == '':
            return HttpResponseRedirect(reverse('booklite:index'))
        print('!'*100)
        print(next)
        return HttpResponseRedirect(next)
    return HttpResponseRedirect(reverse('booklite:registration'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('booklite:index'))


@login_required
def my_books(request):
    books = request.user.books.all()
    return render(request, 'booklite/my_books.html', {'books': books})


def remove_book(request, book_id):
    book = request.user.books.get(id=book_id)
    request.user.books.remove(book)

    return HttpResponseRedirect(reverse('booklite:my_books'))


def book_details(request, book_id):
    book = request.user.books.get(id=book_id)

    return render(request, 'booklite/book_details.html', {'book': book})
