from rest_framework import serializers
from .models import Tmax,Tmin,Rainfall

class TmaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tmax
        fields = '__all__'

class TminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tmin
        fields = '__all__'

class RainfallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rainfall
        fields = '__all__'

