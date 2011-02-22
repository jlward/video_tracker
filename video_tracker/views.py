from django.http import HttpResponse, HttpResponseBadRequest
from video_tracker.models import Video

def mark_all(request):
    if request.method != 'POST':
        return HttpResponseBadRequest()

    user = request.user
    videos = Video.objects.all()
    for video in videos:
        video.add_user(user)
    return HttpResponse()
