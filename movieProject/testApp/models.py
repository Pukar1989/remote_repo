from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=90)
    hero=models.CharField(max_length=90)
    heroine=models.CharField(max_length=90)
    rating=models.IntegerField()
