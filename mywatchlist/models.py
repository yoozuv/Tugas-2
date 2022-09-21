from platform import release
from turtle import title
from django.db import models

class MyWatchlistItem(models.Model):
    watched= models.TextField(max_length=255)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()
    