__all__ = []

from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Sum
from users.models import CustomUser


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def videos(self):
        return (self.get_queryset()
                .filter(content_type__model='videos'))


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Dislike'),
        (LIKE, 'Like'),
    )

    vote = models.SmallIntegerField(choices=VOTES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()

    class Meta:
        verbose_name = 'Like / Dislike'
        verbose_name_plural = 'Likes / Dislikes'

        unique_together = ('user', 'content_type', 'object_id')


class Comment(models.Model):
    video = models.ForeignKey(
        'videos.Videos',
        on_delete=models.CASCADE,
        related_name='comments',
        db_index=True,
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='comments',
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='replies',
        null=True,
        blank=True,
        db_index=True,
    )
    content = models.TextField()
    votes = GenericRelation(LikeDislike, related_query_name='videos')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['video_id', '-created_at']),
            models.Index(fields=['parent_id']),
        ]

    def __str__(self):
        return f'Comment by {self.user.username} on {self.video.title}'
