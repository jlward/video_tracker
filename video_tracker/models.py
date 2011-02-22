from django.db import models

class Video(models.Model):
    name = models.SlugField(unique=True)

    url = models.URLField()

    def __unicode__(self):
        return self.name
