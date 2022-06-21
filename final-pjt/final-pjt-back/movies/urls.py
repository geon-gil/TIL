from django.urls import path
from . import views

urlpatterns = [
    path('limit/<int:limit>/', views.movie_list),
    path('<int:pk>/', views.movie_detail),
    path('<int:pk>/like/', views.like_movie),
    path('<int:pk>/rating/', views.rating_movie),
    path('<int:pk>/rating/<int:rating_pk>/', views.rating_update_or_delete),

    path('<int:pk>/review/', views.review_create),
    path('<int:pk>/review/<int:review_pk>/', views.review_detail_or_update_or_delete),
    path('review/<int:review_pk>/like/', views.like_review),
    path('review/<int:review_pk>/unlike/', views.unlike_review),

    path('<int:review_pk>/comment/', views.comment_list_or_create),
    path('<int:review_pk>/comment/<int:comment_pk>/', views.comment_update_or_delete),

    path('search/<movie_name>/', views.search_movie),

    path('recommended/', views.movie_recommendation),
]
