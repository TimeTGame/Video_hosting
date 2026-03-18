__all__ = ['user_thumbnails_path', 'user_videos_path']

from django.conf import settings


USER_MEDIA_URL = settings.USER_MEDIA_URL


def user_thumbnails_path(instance, filename):
    return USER_MEDIA_URL / f'{instance.user.id}' / 'thumbnails' / filename


def user_videos_path(instance, filename):
    return USER_MEDIA_URL / f'{instance.video.user.id}' / 'videos' / filename
