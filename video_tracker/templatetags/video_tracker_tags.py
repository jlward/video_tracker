from django import template

from video_tracker.models import Video

register = template.Library()

@register.simple_tag
def get_video_link(name, user):
    try:
        video = Video.objects.get(name=name)
    except Video.DoesNotExist:
        return ''
    return '''
	<a onclick="show_video('%s')" href="#">Watch Video</a> |
    ''' % video.url

@register.simple_tag
def get_video(name, user):
    # Dont show the pop up for guest users
    if user.profile.is_guest:
        return ''
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

# For get_video_list the first argument is one space seperated string
@register.simple_tag
def get_video_list(names):
    names = names.split(' ')
    videos = Video.objects.filter(name__in=names).order_by('name')
    list_items = ','.join(['["%s", "%s"]' %(video.url, video) for video in videos])
    if not videos.exists():
        return ''
    return '''
        <a id="watch_video" href="#">Watch Video</a> |
        <script type="text/javascript">
            $('#watch_video').click(function() {
                var items = [%s];
                self.show_video_list(items);
            });
        </script>
    ''' % list_items
