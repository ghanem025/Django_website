from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    headline = models.CharField(max_length=150)
    by_who = models.CharField(max_length=60)
    body_text = models.TextField()
    footer = models.CharField(max_length=50)
    date = models.DateField()
