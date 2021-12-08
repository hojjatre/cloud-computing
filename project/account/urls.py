from django.urls import path
from rest_framework import views
from account import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.Logout.as_view()),
    path('register/', views.Register.as_view()),
]