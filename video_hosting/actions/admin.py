__all__ = []

from django.contrib import admin

from .models import LikeDislike


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'user']
    search_fields = [
        'user__username', 'user__email', 'object_id', 'content_type',
    ]
