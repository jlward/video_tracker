from django import template

from video_tracker.models import Video

register = template.Library()

#TODO Always dont show to guest user
@register.simple_tag
def get_video_url(name, user):
    video = Video.objects.get(name=name)
    return video.url

@register.simple_tag
def get_video(name, user):
    video = Video.objects.get(name=name)
    if user in video.users_viewed.all():
        return ''
    video.add_user(user)
    return '''
	<script type="text/javascript">
		$(document).ready(function() {
			show_video("%s");
		});
	</script>''' % video.url

