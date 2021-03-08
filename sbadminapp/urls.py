
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home-page/',home_page, name='home_page'),
    path('',user_login, name='user_login'),

    

]
