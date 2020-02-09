from django.db import models

class Movie(models.Model):
    not_rated = 0
    rated_g = 1
    rated_pg = 2
    rated_r = 3
    ratings = (
        (not_rated, 'NR - Not Rated'),
        (rated_g, 'G - General Audiences'),
        (rated_pg, 'PG - Parental Guidance Suggested'),
        (rated_r, 'R - Restricted'),)
    title = models.CharField( max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices = ratings, default = not_rated)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    class Meta:
        ordering = ('-year', 'title')


    def __str__(self):
        return '{} ({})'.format(self.title, self.year)
