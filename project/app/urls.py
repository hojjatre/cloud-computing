from django.urls import path
from rest_framework import views
from app import views as app_view


urlpatterns = [
    path('login/', app_view.login),
    path('logout/', app_view.Logout.as_view()),
    path('register/', app_view.Register.as_view()),
    path('show/', app_view.ShowUser.as_view()),
    path('gamesRank/<int:rank>', app_view.ShowGamesByRanking.as_view()),
    path('gamesName/<str:name>', app_view.ShowGamesByName.as_view()),
    path('bestGame/', app_view.NbestGameinEveryYear.as_view()),
    path('fiveBestGame/', app_view.FiveBestGameForOnePlatformInParticularYear.as_view()),
    path('euGTna/', app_view.EuGtNa.as_view()),
]