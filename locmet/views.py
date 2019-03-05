from django.shortcuts import render
from rest_framework import generics
from .serializers import TmaxSerializer,TminSerializer,RainfallSerializer
from .models import Tmax,Tmin,Rainfall

# Create your views here.


class RainfallMatrice(generics.ListAPIView):

    serializer_class = RainfallSerializer

    def get_queryset(self):
        location = self.kwargs.get('location',None)
        return Rainfall.objects.filter(location = location)


class TmaxMatrice(generics.ListAPIView):

    serializer_class = TmaxSerializer

    def get_queryset(self):
        location = self.kwargs.get('location')
        return Tmax.objects.filter(location = location)


class TminMatrice(generics.ListAPIView):

    serializer_class = TminSerializer

    def get_queryset(self):
        location = self.kwargs.get('location',None)
        return Tmin.objects.filter(location = location)
