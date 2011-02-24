import json
import string
import re

from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    name = models.SlugField(unique=True)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    thumbnail_url = models.URLField()

    url = models.URLField()

    users_viewed = models.ManyToManyField(User, null=True, db_table="user_have_viewed")

    def __unicode__(self):
        return self.title

    def add_user(self, user):
        self.users_viewed.add(user)

    @classmethod
    def from_json(cls, name, data):
        data = data.strip(string.ascii_letters + '_();\n')
        data = re.sub(r'/\*.*?\*/', '', data)

        data = json.loads(data)[0]
        post = data['Post']
        Video.objects.create(
            name=name,
            title=post['title'],
            description=post['description'].strip(' ;'),
            thumbnail_url=post['thumbnail120Url'],
            url=post['embedUrl'],
        )
