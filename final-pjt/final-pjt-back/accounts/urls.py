from django.urls import path
from . import views


urlpatterns = [
    path('profile/<username>/', views.profile),
    path('signout/', views.signout),
]
