from django.contrib import admin
from django.urls import path,include
from .views import page_search

urlpatterns = [
    path('', page_search),
]