from django.views.generic import ListView, DetailView
from .models import Person, Movie


class PersonDetailView(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()


class MovieListView(ListView):
    model = Movie


class MovieDetailView(DetailView):
    queryset = Movie.objects.all_with_related_persons()
