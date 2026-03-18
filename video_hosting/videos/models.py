__all__ = []

from django.db import models
from users.models import CustomUser


class Videos(models.Model):
    STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('public', 'Public'),
        ('private', 'Private'),
        ('unlisted', 'Unlisted'),
        ('blocked', 'Blocked'),
    )

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='videos',
        db_index=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextChoices(blank=True)
    thumbnail = models.URLField(max_length=500, blank=True, null=True)
    duration_seconds = models.PositiveBigIntegerField()
    views_count = models.PositiveBigIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='processing',
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'videos'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user_id', '-created_at']),
            models.Index(fields=['-views_count']),
            models.Index(fields=['status', '-created_at']),
        ]

    def __str__(self):
        return f'{self.title} ({self.user.username})'


class VideoFiles(models.Models):
    FORMAT_CHOICES = (
        ('mp4', 'MP4'),
        ('hls', 'HLS'),
        ('dash', 'DASH'),
    )

    resolution = models.CharField(max_length=10)
    video_format = models.CharField(
        max_length=10, choices=FORMAT_CHOICES, default='mp4',
    )
    storage_url = models.URLField(max_length=500)

    class Meta:
        db_table = 'video_files'
        indexes = [
            models.Index(fields=['video_id', 'resolution']),
        ]

    def __str__(self):
        return f'{self.video.title} - {self.resolution}'
