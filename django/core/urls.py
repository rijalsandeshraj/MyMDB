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
    path('movie/<int:movie_id>/vote',
         views.CreateVote.as_view(),
         name='create_vote'),
    path('movie/<int:movie_id/vote/<int:pk>',
         views.UpdateVote.as_view(),
         name='update_vote')
]
