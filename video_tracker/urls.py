from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('video_tracker.views',
    url(r'^$', 'mark_all',
        name='video_tracker_mark_all'),
)

