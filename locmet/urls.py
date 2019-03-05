from django.conf.urls import url
from django.urls import path
from .views import RainfallMatrice,TmaxMatrice,TminMatrice
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'locmet'

urlpatterns = [
    path('rainfall/<str:location>/',RainfallMatrice.as_view(), name = 'rainfall-locationwise-list'),
    path(r'tmax/<str:location>/',TmaxMatrice.as_view(), name = 'tmax-locationwise-list'),
    path('tmin/<str:location>/',TminMatrice.as_view(), name = 'tmin-locationwise-list')
]