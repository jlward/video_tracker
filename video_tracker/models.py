from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.SlugField(unique=True)

    url = models.URLField()

    users_viewed = models.ManyToManyField(User, null=True, db_table="user_have_viewed")

    def __unicode__(self):
        return self.name

    def add_user(self, user):
        self.users_viewed.add(user)
