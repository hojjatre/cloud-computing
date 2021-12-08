from django.urls import path
from rest_framework import views
from main_service import views as main_view


urlpatterns = [
    path('gamesRank/<int:rank>', main_view.ShowGamesByRanking.as_view()),
    path('gamesName/<str:name>', main_view.ShowGamesByName.as_view()),
    path('bestGame/', main_view.NbestGameinEveryYear.as_view()),
    path('fiveBestGame/', main_view.FiveBestGameForOnePlatformInParticularYear.as_view()),
    path('euGTna/', main_view.EuGtNa.as_view()),
]