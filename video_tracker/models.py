from django.db import models

class Video(models.Model):
    name = models.SlugField(unique=True)
