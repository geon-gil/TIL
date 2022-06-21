from email import header
import requests
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
django.setup()
from movies.models import Movie, Genre


# tmdb에서 장르 데이터 json으로 저장
def genre_data_request():
    secret_file = 'secrets.json'
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    TMDB_API_KEY = secrets['TMDB_API_KEY']
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/genre/movie/list'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'ko',
    }
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    response = requests.get(BASE_URL + path, params=params, headers=headers)
    data = response.json()
    results_list = data.get('genres')
    return results_list


# genre 데이터 json 형식으로 작성
def get_genre_data():
    genre_list = genre_data_request()

    result = []
    genre_dict = {}
    for genre in genre_list:
        if not Genre.objects.filter(pk=genre.get("id")).exists():
            genre_dict = {
                "model" : "movies.genre",
                "pk" : genre.get("id"),
                "fields" : {
                    "name" : genre.get("name")
                }
            }
        result.append(genre_dict)
    return result 


# tmdb에서 영화 정보 받아서 json으로 저장
def movie_data_request(page):
    secret_file = 'secrets.json'
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    TMDB_API_KEY = secrets['TMDB_API_KEY']
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/top_rated'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'ko',
        'page': page
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    response = requests.get(BASE_URL + path, params=params, headers=headers)
    data = response.json()
    results_list = data.get('results')
    return results_list


# 배우, 감독 데이터 json으로 저장
def actor_director_data_request(movie_id):
    secret_file = 'secrets.json'
    with open(secret_file) as f:
        secrets = json.loads(f.read())
    TMDB_API_KEY = secrets['TMDB_API_KEY']
    BASE_URL = 'https://api.themoviedb.org/3'
    path = f'/movie/{movie_id}/credits'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'ko',
    }

    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }

    response = requests.get(BASE_URL + path, params=params, headers=headers)
    data = response.json()
    cast_list = data.get('cast')
    director_list = data.get('crew')

    director_data = []
    for idx in range(len(director_list)):
        if director_list[idx]['job'] == 'Director':
            director_data.append(director_list[idx])
            break
    return cast_list, director_data


# json 파일로 저장할 영화, 배우, 감독 데이터 
def get_top_rated_movie_data():
    movie_result = []
    actor_result = []
    director_result = []
    for page in range(1, 50):
        results_list = movie_data_request(page)
        for movie in results_list:
            if not Movie.objects.filter(pk=movie.get("id")).exists():
                actors_list, directors_list = actor_director_data_request(movie.get("id"))
                actors = []
                len_actor_list = 0
                if 5 < len(actors_list):
                    len_actor_list = 5
                else:
                    len_actor_list = len(actors_list)
                for idx in range(len_actor_list):
                    actors.append(actors_list[idx].get("id"))
                    actor_dict = {
                        "model" : "movies.actor",
                        "pk" : actors_list[idx].get("id"),
                        "fields" : {
                            "name" : actors_list[idx].get("name"),
                            "profile_path" : actors_list[idx].get("profile_path"),
                        }
                    }
                    actor_result.append(actor_dict)
                directors = []
                directors.append(directors_list[0].get("id"))
                director_dict = {
                    "model" : "movies.director",
                        "pk" : directors_list[0].get("id"),
                        "fields" : {
                            "name" : directors_list[0].get("name"),
                            "profile_path" : directors_list[0].get("profile_path"),
                        }
                }
                director_result.append(director_dict) 
                movie_dict = {
                    "model" : "movies.movie",
                    "pk" : movie.get("id"),
                    "fields" : {
                        "title" : movie.get("title"),
                        "release_date" : movie.get("release_date"),
                        "vote_count" : movie.get("vote_count"),
                        "vote_average" : movie.get("vote_average"),
                        "popularity" : movie.get("popularity"),
                        "overview" : movie.get("overview"),
                        "poster_path" : movie.get("poster_path"),
                        "like_users" : [],
                        "genres" : movie.get("genre_ids"),
                        "actors" : actors,
                        "directors" : directors,
                    }
                }
                movie_result.append(movie_dict)
    return movie_result, actor_result, director_result


movie_result, actor_result, director_result = get_top_rated_movie_data()

with open('movies/fixtures/movies/movies.json', 'w', encoding="UTF=8") as f:
    json.dump(movie_result, f, ensure_ascii=False, indent = 2)

with open('movies/fixtures/movies/genres.json', 'w', encoding="UTF=8") as f:
    json.dump(get_genre_data(), f, ensure_ascii=False, indent = 2)

with open('movies/fixtures/movies/actors.json', 'w', encoding="UTF=8") as f:
    json.dump(actor_result, f, ensure_ascii=False, indent = 2)

with open('movies/fixtures/movies/directors.json', 'w', encoding="UTF=8") as f:
    json.dump(director_result, f, ensure_ascii=False, indent = 2)