from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=50)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)


class Director(models.Model):
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200, null=True)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)   
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    genres = models.ManyToManyField(Genre, related_name='movie_genre') 
    actors = models.ManyToManyField(Actor, related_name='movie_actor')
    directors = models.ManyToManyField(Director, related_name='movie_directors')
    user_rating = models.FloatField(default=0)

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    not_like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='not_like_reviews')


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Weather(models.Model):
    forecast = models.CharField(max_length=10)
    genres = models.ManyToManyField(Genre, related_name='weather_genre') 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Rating(models.Model):
    score = models.DecimalField(
        default=0, 
        validators=[MinValueValidator(0), MaxValueValidator(10)], 
        max_digits=3, 
        decimal_places=1
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)