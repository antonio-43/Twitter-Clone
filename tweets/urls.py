from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # index
    path('tweeting/', views.make_tweet, name='tweeting'),
    path('show/', views.show_tweets, name='show_tweets'),
]
