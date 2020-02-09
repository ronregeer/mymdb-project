from django.shortcuts import render

from django.views.generic import (
    ListView, DetailView,
)

from core.models import Movie

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    paginate_by = 10
    model = Movie





# class PersonDetail(DetailView):
#     queryset = Person.objects.all_with_prefetch_movies()
