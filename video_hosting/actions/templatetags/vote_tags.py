__all__ = []

from django import template

register = template.Library()


@register.filter(name='has_liked')
def has_liked(user, obj) -> bool:
    user_vote = obj.votes.filter(user=user)

    if user_vote.exists() and user_vote[0].vote == 1:
        return True
    else:
        return False


@register.filter(name='has_disliked')
def has_disliked(user, obj) -> bool:
    user_vote = obj.votes.filter(user=user)

    if user_vote.exists() and user_vote[0].vote == -1:
        return True
    else:
        return False
