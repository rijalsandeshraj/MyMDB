from django.views.generic.list import ListView
from .models import Movie


class MovieListView(ListView):
    model = Movie
