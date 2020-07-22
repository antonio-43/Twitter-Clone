from django.urls import path

from .views import create_user, log_user
from . import views

urlpatterns = [
    path('newuser/', views.create_user, name='novo_user'),
    path('login/', views.log_user, name='log_user'),
]
