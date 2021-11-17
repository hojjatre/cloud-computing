from django.urls import path
from rest_framework import views
from app import views as app_view


urlpatterns = [
    path('login/', app_view.login),
    path('logout/', app_view.Logout.as_view()),
    path('register/', app_view.Register.as_view()),
    path('show/', app_view.ShowUser.as_view()),
]