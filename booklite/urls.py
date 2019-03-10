from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'booklite'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_book/', views.save_book, name='save_book'),
    path('register_user/', views.register_user, name='register_user'),
    path('registration/', views.registration, name='registration'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('my_books/', views.my_books, name='my_books'),    
    path('<int:book_id>/book_details/', views.book_details, name="book_details"),
    path('<int:book_id>/remove_book/', views.remove_book, name="remove_book")
]