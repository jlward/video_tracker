from django import template

from video_tracker.models import Video

register = template.Library()

@register.simple_tag
def get_video_url(name):
    video = Video.objects.get(name=name)
    return video.url
