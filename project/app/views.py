from django.db.models import Count
from django.http.response import HttpResponse
from rest_framework import permissions
from django.db.models import F
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework import generics, serializers
from .serializers import UserSerializer, VgSalesSerialier
from django.db.models import Avg, Sum, Max, Min
from .models import User, vgSales
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
import numpy as np
import matplotlib.pyplot as plt
login = obtain_auth_token

class Logout(APIView):
    """
    Delete user's authtoken
    """
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={'message': f"Bye {request.user.username}!"}, status=HTTP_200_OK)

class ShowUser(ListAPIView):
    """
    Show users
    """
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

class Register(CreateAPIView):
    """
    Create a new user
    """
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

class ShowGamesByRanking(APIView):

    serializer_class = VgSalesSerialier
    permission_classes = (IsAuthenticated,)


    def get(self, request, rank):

        temp = vgSales.objects.filter(id=rank)
        
        return Response(data={
            'name': f"{temp.get().Name}",
            'Platform': f"{temp.get().Platform}" ,
            'Year': f"{temp.get().Year}",
            'Genre': f"{temp.get().Genre}",
            'Publisher': f"{temp.get().Publisher}",
            'NA_Sales': f"{temp.get().NA_Sales}",
            'EU_Sales': f"{temp.get().EU_Sales}",
            'JP_Sales': f"{temp.get().JP_Sales}",
            'Other_Sales': f"{temp.get().Other_Sales}",
            'Global_Sales': f"{temp.get().Global_Sales}",
            })


class ShowGamesByName(APIView):
    serializer_class = VgSalesSerialier
    permission_classes = (IsAuthenticated,)


    def get(self, request, name):
        temp = vgSales.objects.filter(Name__contains = name)
        
        name = []
        platform = []
        year = []
        genre = []
        publisher = []
        na_sales = []
        eu_sales = []
        jp_sales = []
        other_sales = []
        global_sales = []
        for game in temp:
            name.append(game.Name)
            platform.append(game.Platform)
            year.append(game.Year)
            genre.append(game.Genre)
            publisher.append(game.Publisher)
            na_sales.append(game.NA_Sales)
            eu_sales.append(game.EU_Sales)
            jp_sales.append(game.JP_Sales)
            other_sales.append(game.Other_Sales)
            global_sales.append(game.Global_Sales)


        return Response(data={
            'name': f"{name}",
            'Platform': f"{platform}" ,
            'Year': f"{year}",
            'Genre': f"{genre}",
            'Publisher': f"{publisher}",
            'NA_Sales': f"{na_sales}",
            'EU_Sales': f"{eu_sales}",
            'JP_Sales': f"{jp_sales}",
            'Other_Sales': f"{other_sales}",
            'Global_Sales': f"{global_sales}",
            })

    
class NbestGameinEveryYear(APIView):
    serializer_class = VgSalesSerialier
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        # example -> Get : http://127.0.0.1:8000/bestGame?N=5&Which=Platform
        # another example : http://127.0.0.1:8000/bestGame?N=5&Which=Year
        n = request.GET.get('N')
        which = request.GET.get('Which')
        games = vgSales.objects.values(which).annotate(count=Count(which))
        re_which = []
        for game in games:
            if game != "N/A":
                re_which.append(game.get(which))

        all_vgSales = []
        temp = []
        for w in re_which:
            if which == "Platform":
                all_vgSales = vgSales.objects.filter(Platform=w).order_by('id')
            elif which == "Genre":
                all_vgSales = vgSales.objects.filter(Genre=w).order_by('id')
            elif which == "Year":
                if w != 'N/A':
                    all_vgSales = vgSales.objects.filter(Year=w).order_by('id')
            t = all_vgSales[:int(n)]
            for all in t:
                temp.append(f"{w} : name: {all.Name}")
        
        return Response(data=
            {
                'result':f"{temp},"
            }
        )

class FiveBestGameForOnePlatformInParticularYear(APIView):
    serializer_class = VgSalesSerialier
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        #example Get: http://127.0.0.1:8000/fiveBestGame?year=2006&platform=Wii
        year = request.GET.get('year')
        platform = request.GET.get('platform')

        games = vgSales.objects.filter(Platform=platform).filter(Year=year).order_by('id')

        result = []

        for game in games[0:5]:
            result.append(f"name: {game.Name}")
        

        return Response(data=
            {
                'result': result,
            }
        )


class EuGtNa(APIView):
    serializer_class = VgSalesSerialier
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        games = vgSales.objects.filter(EU_Sales__gt=F('NA_Sales'))

        result = []

        for game in games:
            result.append(f"name: {game.Name}")
        

        return Response(data=
            {
                'result': result,
            }
        )