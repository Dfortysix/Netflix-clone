from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'movie'

urlpatterns = [
   path("",views.MovieList,name="movielist"),
   path('<int:pk>/',views.detail,name="detail"),
   path('play/<str:movie_id>/',views.Playmovie, name="play-movie"),
   path("tvshows",views.Tvshow,name="tvshows"),
   path("latest",views.LatestMovie,name="latest"),
   path("mylist",views.Mylist,name="mylist"),


]