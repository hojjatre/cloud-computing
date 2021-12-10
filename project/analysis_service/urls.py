from django.urls import path
from rest_framework import views
from analysis_service import views as app_view


urlpatterns = [
    path('comparison/<str:name_game1>/<str:name_game2>', app_view.ComparisonTwoGames.as_view()),
    path('totalsales/<int:yearOne>/<int:yearTwo>', app_view.TotalSalesEachYear.as_view()),
    path('comparisonpublisher/<int:yearOne>/<int:yearTwo>/<str:publisherOne>/<str:publisherTwo>', app_view.TotalSalesBetweenPublisherEachYear.as_view()),
    path('totalsalesGenre/<int:yearOne>/<int:yearTwo>',app_view.TotalSalesBetweenGenreEachYear.as_view()),
]