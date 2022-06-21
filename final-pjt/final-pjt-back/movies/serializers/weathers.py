from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Weather, Genre

User = get_user_model()


class WeatherSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    class GenreListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = '__all__'
    
    genres = GenreListSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Weather
        fields = '__all__'