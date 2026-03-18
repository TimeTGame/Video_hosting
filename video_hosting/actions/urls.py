from django.contrib.auth.decorators import login_required
from django.urls import re_path
from videos.models import Videos

from . import views
from .models import LikeDislike


app_name = 'actions'

urlpatterns = [
    re_path(
        r'^video/(?P<pk>\d+)/like/$',
        login_required(
            views.VotesView.as_view(model=Videos, vote_type=LikeDislike.LIKE),
        ),
        name='video_like',
    ),
    re_path(
        r'^video/(?P<pk>\d+)/dislike/$',
        login_required(
            views.VotesView
            .as_view(model=Videos, vote_type=LikeDislike.DISLIKE),
        ),
        name='video_dislike',
    ),
]
