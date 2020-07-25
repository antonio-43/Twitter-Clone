from django.db import models

class user(models.Model):

    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
