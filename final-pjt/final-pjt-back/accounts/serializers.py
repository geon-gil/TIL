from rest_framework import serializers
from django.contrib.auth import get_user_model

from movies.models import Movie, Review, Genre

class UserSerializer(serializers.ModelSerializer):

    class MovieSerializer(serializers.ModelSerializer):
        
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
                'poster_path',
                'vote_average',
                'genres'
        )
    class ReviewListSerializer(serializers.ModelSerializer):

        class Meta:
            model = Review
            fields = '__all__'
            read_only_fields = ('movie', 'like_users', 'not_like_users', )

    review_set = ReviewListSerializer(many=True, read_only=True)
    like_movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'like_movies',
            'review_set',
        )