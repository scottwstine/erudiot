from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'booklite'
urlpatterns = [
    path('', views.index, name='index'),
    path('save_book/', views.save_book, name='save_book'),
    path('register_user/', views.register_user, name='register_user'),
    path('registration/', views.registration, name='registration')
]