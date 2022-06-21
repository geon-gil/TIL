from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Comment, Genre, Weather, Rating
from .serializers.movies import MovieListSerializer, MovieDetailSerializer, RatingSerializer
from .serializers.reviews import ReviewListSerializer
from .serializers.comments import CommentListSerializer
from .serializers.weathers import WeatherSerializer
from accounts.serializers import UserSerializer

from .weather_api import weather_data_request
import requests


@api_view(['GET'])
def movie_list(request, limit):
    movies = Movie.objects.order_by('-popularity')[:limit]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    serializer = MovieDetailSerializer(movie)
    rating_set = serializer.data.get('rating_set')
    rating_count = serializer.data.get('rating_count')

    if rating_count:
        total_score = 0
        score = []
        for i in range(len(rating_set)):
            score.append(float(rating_set[i].get('score')))
        total_score = round(sum(score) / rating_count, 2)
        movie.user_rating = total_score
        movie.save()
        serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def like_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        movie.like_users.add(user)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
def rating_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user
    
    if request.method == 'POST':
        rates = Rating.objects.filter(user=user, movie=movie)
        if rates:
            rate = Rating.objects.get(user=user, movie=movie)
            serializer = RatingSerializer(instance=rate, data=request.data)
            if serializer.is_valid(raise_exception=True):
                data = serializer.save(movie=movie, user=user)
                movie = get_object_or_404(Movie, pk=pk)
                serializer = MovieDetailSerializer(movie)
                rating_set = serializer.data.get('rating_set')
                rating_count = serializer.data.get('rating_count')
                if rating_count:
                    total_score = 0
                    score = []
                    for i in range(len(rating_set)):
                        score.append(float(rating_set[i].get('score')))
                    total_score = round(sum(score) / rating_count, 2)
                    movie.user_rating = total_score
                    movie.save()
                    data.movie = movie
                    data.save()
                    serializer = RatingSerializer(data)
                return Response(serializer.data)

        rating = request.data
        serializer = RatingSerializer(data=rating)
        if serializer.is_valid(raise_exception=True):
            data = serializer.save(movie=movie, user=user)
            movie = get_object_or_404(Movie, pk=pk)
            serializer = MovieDetailSerializer(movie)
            rating_set = serializer.data.get('rating_set')
            rating_count = serializer.data.get('rating_count')
            if rating_count:
                total_score = 0
                score = []
                for i in range(len(rating_set)):
                    score.append(float(rating_set[i].get('score')))
                total_score = round(sum(score) / rating_count, 2)
                movie.user_rating = total_score
                movie.save()
                data.movie = movie
                data.save()
                serializer = RatingSerializer(data)
            return Response(serializer.data)



@api_view(['PUT', 'DELETE'])
def rating_update_or_delete(request, pk, rating_pk):
    rating = Rating.objects.get(pk=rating_pk)

    if request.method == 'PUT':
        if request.user == rating.user:
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                data = serializer.save()
                movie = get_object_or_404(Movie, pk=pk)
                serializer = MovieDetailSerializer(movie)
                rating_set = serializer.data.get('rating_set')
                rating_count = serializer.data.get('rating_count')
                if rating_count:
                    total_score = 0
                    score = []
                    for i in range(len(rating_set)):
                        score.append(float(rating_set[i].get('score')))
                    total_score = round(sum(score) / rating_count, 2)
                    movie.user_rating = total_score
                    movie.save()
                    data.movie = movie
                    data.save()
                    serializer = RatingSerializer(data)
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if request.user == rating.user:
            rating.delete()
            data = {
                'message': '평점이 삭제되었습니다.'
            }
            return Response(data=data)


@api_view(['POST'])
def review_create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user

    if request.method == 'POST':
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie, user=user)
            
            reviews = movie.reviews.order_by('-pk')
            serializer = ReviewListSerializer(reviews, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_or_update_or_delete(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if user == review.user:
            serializer = ReviewListSerializer(instance=review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=user)
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if user == review.user:
            review.delete()
            data = {
                'message': '리뷰가 삭제되었습니다.'
            }
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.not_like_users.filter(pk=user.pk).exists():
        serializer = ReviewListSerializer(review)
    else:
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            serializer = ReviewListSerializer(review)
            return Response(serializer.data)
        else:
            review.like_users.add(user)
            serializer = ReviewListSerializer(review)
            return Response(serializer.data)


@api_view(['POST'])
def unlike_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user
    if review.like_users.filter(pk=user.pk).exists():
        serializer = ReviewListSerializer(review)
        return Response(serializer.data)
    else:
        if review.not_like_users.filter(pk=user.pk).exists():
            review.not_like_users.remove(user)
            serializer = ReviewListSerializer(review)
            return Response(serializer.data)
        else:
            review.not_like_users.add(user)
            serializer = ReviewListSerializer(review)
            return Response(serializer.data)


@api_view(['GET', 'POST'])
def comment_list_or_create(request, review_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        comments = review.comment_set.order_by('-pk')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=user)

            comments = review.comment_set.order_by('-pk')
            serializer = CommentListSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, review_pk, comment_pk):
    user = request.user
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'PUT':
        if user == comment.user:
            serializer = CommentListSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(review=review, user=user)
                comments = review.comment_set.order_by('-pk')
                serializer = CommentListSerializer(comments, many=True)
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if user == comment.user:
            comment.delete()
            comments = review.comment_set.order_by('-pk')
            serializer = CommentListSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_movie(request, movie_name):
    movies = Movie.objects.all()
    search_movie = Movie.objects.filter(title__contains=movie_name)
    # 검색한 영화가 없을 경우
    if search_movie:
        # 검색한 영화가 있는 경우 해당 영화 return 
        serializer = MovieDetailSerializer(search_movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    movies = Movie.objects.order_by('-popularity')[:10]
    recommend_serializer = MovieDetailSerializer(movies, many=True)
    return Response(recommend_serializer.data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def movie_recommendation(request):
    user = request.user
    user_serializer = UserSerializer(user)

    def user_weather(user):
        BASE_URL = 'http://ip-api.com/json'
        data = requests.get(BASE_URL)
        loc_data = data.json()
        nx = loc_data.get('lat')
        ny = loc_data.get('lon')

        result = weather_data_request(nx, ny)
        forecast = ''

        if result['rain'] != '강수없음':
            forecast = 'rainy'
        elif 30 <= result['tmp']:
            forecast = 'hot'
        elif result['tmp'] < 0:
            forecast = 'cold'
        elif result['sky'] == 1:
            forecast = 'sunny'
        elif result['sky'] == 2:
            forecast = 'cloudy'
        else:
            forecast = 'foggy'
        weather_genre = {
            'rainy': [
                27, 
                28,
                35,
                10402
            ],
            'hot': [
                53,
                10752,
                10770
            ],
            'cold': [
                99,
                10749,
                10751
            ],
            'sunny': [
                12, 
                14,
                16,
                18
            ],
            'cloudy': [
                36,
                37
            ],
            'foggy': [
                80,
                878,
                9648
            ]
        }
        if Weather.objects.filter(user=user).exists():
            weather = Weather.objects.get(user=user)
            return Response(weather)
        weather = Weather()
        weather.forecast = forecast
        weather.user = user
        weather.save()
        weather.genres.set(weather_genre.get(forecast))
        weather.save()
        return Response(weather)


    if user_serializer.data.get("like_movies"):
        user_like_movies = user_serializer.data.get("like_movies")
        user_like_genre = {
            12: 0,
            14: 0,
            16: 0,
            18: 0,
            27: 0,
            28: 0,
            35: 0,
            36: 0,
            37: 0,
            53: 0,
            80: 0,
            99: 0,
            878: 0,
            9648: 0,
            10402: 0,
            10749: 0,
            10751: 0,
            10752: 0,
            10770: 0,
        }
        favorite_genre = 0
        for item in user_like_movies:
            for key in user_like_genre:
                for ids in item.get('genres'):
                    if key == ids.get('id'):
                        user_like_genre[key] += 1
                if favorite_genre < user_like_genre[key]:
                    favorite_genre = key
        genres = Genre.objects.filter(pk=favorite_genre)
        movies = Movie.objects.filter(genres__in=genres).order_by('-popularity')[:30]
        movie_serializer = MovieDetailSerializer(movies, many=True)
        return Response(movie_serializer.data)

    user_weather(user)
    weather = Weather.objects.get(user=user).genres.all()[:1]
    genres = Genre.objects.filter(pk=weather)
    movies = Movie.objects.filter(genres__in=genres).order_by('-popularity')[:30]
    movie_serializer = MovieDetailSerializer(movies, many=True)
    return Response(movie_serializer.data)



