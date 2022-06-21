## 1. DB에 기본 데이터 추가

- secrets.json에 api key 추가 후 저장(manage.py랑 같은 위치에 파일 두기)
- migrate 후에 `python manage.py loaddata movies/movies.json movies/actors.json movies/directors.json movies/genres.json`
- tmdb에 영상 데이터 없는 경우에만 유튜브에서 받아오는 방식으로 작성해뒀으나 현재 할당량 부족으로 주석처리 해둠
  - 현재 데이터에 영상 아이디 중 null 값 있음

- api key
  - search url로 접근하지 않는 경우에는 youtube, tmdb api key 없어도 동작함
  - db에 json 파일을 통해 저장하기 때문


- 현재 search url을 만들어뒀는데 영화 검색만 가능
  - db에 영화 데이터가 있으면 해당 데이터 반환
  - 없을 경우
    - 유저가 좋아요한 영화의 장르데이터 기반 추천
    - 좋아요한 영화가 없을 경우
      - 전체 데이터 중 popularity 기준으로 영화 반환



## 2. 오류

- migrations 폴더 안에 migrate 파일이 없는데 `makemigrations` 안되는 경우
  - `python manage.py makemigrations accounts movies` 로 시도
- 토큰이 없다고 뜨는 경우 -> createsuperuser 생성해서 로그인 후 토큰 값 header로 보내기
- `trailer = video_list[0]['id']['videoId'],
  TypeError: 'NoneType' object is not subscriptable`
  - youtube api 키 할당량 초과시 발생하는 오류



## 3. serializer

- movie
  - 전체 데이터 조회
    - title, vote_average, poster_path, trailer, genres
  - 개별 영화 데이터 조회
    - 전체 필드
- review
  - 전체, 개별 동일
    - 전체 필드(user(pk, username), movie, title, content, created_at, updated_at, like_users, not_like_users)

- comment
  - 전체, 개별 동일
    - 전체 필드(user(pk, username), content, review, user)

- accounts
  - username, like_movies(title, poster_path, genres), review_set(all)



## 4. movies / views & urls

- `http://127.0.0.1:8000/api/v1/movies/`	
  - GET
    - 전체 영화 조회
    - vote_average가 높은 순으로 정렬되어 있음
- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/`
  - GET
    - 개별 영화 조회
- `http://127.0.0.1:8000/api/v1/movies/<like>/`
  - POST
    - 해당 영화에 좋아요 표시		
    - 개별 영화 데이터가 return 됨



- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/review/`	
  - GET
    - 영화 역참조, 해당 영화에 작성된 모든 리뷰를 -pk로 정렬
    - 해당 영화에 작성된 리뷰만 조회가능
  - POST
    - 리뷰 작성 시 해당 영화의 전체 리뷰  return
- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/review/<int:review_pk>/`	
  - PUT
    - 해당 영화의 전체 리뷰  return
  - DELETE
    - 해당 영화의 전체 리뷰  return
- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/review/<int:review_pk>/like/`
  -  POST
    - 요청이 들어왔을 때 not_like_users에 존재하지 않는 경우에만 좋아요/좋아요 취소 진행
    - not_like_users에 존재하는 경우 해당 영화의 전체 reivew return 
    - 좋아요/좋아요 취소가 진행된 경우 해당 review 하나만 return 
- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/review/<int:review_pk>/unlike/`
  -  POST
    - 요청이 들어왔을 때 like_users에 존재하지 않는 경우에만 싫어요/싫어요취소 진행
    - like_users에 존재하는 경우 해당 영화의 전체 reivew return 
    - 싫어요/싫어요취소가 진행된 경우 해당 review 하나만 return 



- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/<int:review_pk>/comment/`	
  - GET
    - comment 역참조, 해당 comment 에 작성된 모든 comment 를 -pk로 정렬
  - POST
    - comment 작성 시 해당 review의 모든 comment return
- `http://127.0.0.1:8000/api/v1/movies/<int:pk>/<int:review_pk>/comment/<int:comment_pk>/`
  - PUT
    - 해당 review의 전체 comment return
  - DELETE
    - 해당 review의 전체 comment return 

- `http://127.0.0.1:8000/api/v1/movies/search/<movie_name>/`
  - GET
    - 검색 결과가 있으면 결과 보여줌
    - 없으면 유저가 좋아요한 영화의 장르 기반 추천 영화 보여줌
    - 좋아요한 영화가 없으면 인기 영화 보여줌

## 5. accounts / views & urls

- `http://127.0.0.1:8000/api/v1/accounts/profile/<username>/`
  - GET
    - username, 좋아요한 영화의 title, poster_path, genres 조회 가능

- `http://127.0.0.1:8000/api/v1/accounts/signout/`
  - POST
    - db에서 유저 데이터 삭제