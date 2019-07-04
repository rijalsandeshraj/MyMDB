from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('movies',
         views.MovieListView.as_view(),
         name='movie_list'),
    path('movie/<int:pk>',
         views.MovieDetailView.as_view(),
         name='movie_detail'),
]
