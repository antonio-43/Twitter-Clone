from django.db import models

# Create your models here.


class Tweet(models.Model):

    Title = models.CharField(max_length=500)
    Content = models.CharField(max_length=1024)
