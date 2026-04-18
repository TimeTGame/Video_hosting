__all__ = []

from django.contrib import admin

from .models import Comment, LikeDislike


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ['content_type', 'object_id', 'user']
    search_fields = [
        'user__username', 'user__email', 'object_id', 'content_type',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'video', 'created_at']
    search_fields = [
        'user__username', 'user__email', 'content',
    ]
