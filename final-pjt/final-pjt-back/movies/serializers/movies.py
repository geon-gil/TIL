from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models import Movie, Genre, Actor, Director, Rating
from .reviews import ReviewListSerializer
User = get_user_model()


class MovieListSerializer(serializers.ModelSerializer):

    class GenreListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = '__all__'
    
    genres = GenreListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'vote_average',
            'poster_path',
            'genres'
        )


class MovieDetailSerializer(serializers.ModelSerializer):

    class ActorListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Actor
            fields = '__all__'
    

    class DirectorListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Director
            fields = '__all__'


    class RatingSerializer(serializers.ModelSerializer):

        class Meta:
            model = Rating
            fields = '__all__'

    class GenreListSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Genre
            fields = '__all__'
    
    genres = GenreListSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)
    directors = DirectorListSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)
    rating_set = RatingSerializer(many=True, read_only=True)
    rating_count = serializers.IntegerField(source="rating_set.count", read_only=True) 

    class Meta:
        model = Movie
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = (
                'username',
        )
    
    user = UserSerializer(read_only=True)
    movie = MovieDetailSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'