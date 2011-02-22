from django import template

from video_tracker.models import Video

register = template.Library()

#TODO Always dont show to guest user
@register.simple_tag
def get_video_link(name, user):
    try:
        video = Video.objects.get(name=name)
    except Video.DoesNotExist:
        return ''
    return '''
	<a onclick="show_video(%s)" href="#">Watch Video</a> |
    ''' % video.url

@register.simple_tag
def get_video(name, user):
    try:
        video = Video.objects.get(name=name)
    except Video.DoesNotExist:
        return ''
    if user in video.users_viewed.all():
        return ''
    video.add_user(user)
    return '''
	<script type="text/javascript">
		$(document).ready(function() {
			show_video("%s");
		});
	</script>''' % video.url

