from rest_framework import serializers
from .models import Advert

class AdvertListSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Advert
        fields = '__all__'

class AdvertDetailSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Advert
        fields = '__all__'