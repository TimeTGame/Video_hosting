__all__ = []

from django.contrib import admin

from .models import VideoFiles, Videos


@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    verbose_name = 'Video'
    verbose_name_plural = 'Videos'

    list_display = ['title', 'user', 'views_count']
    list_filter = ['created_at']
    search_fields = ['title', 'user__username', 'user__email', 'description']


@admin.register(VideoFiles)
class VideoFilesAdmin(admin.ModelAdmin):
    list_display = ['storage_url']
