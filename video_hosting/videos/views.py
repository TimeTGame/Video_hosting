__all__ = []

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from videos.models import VideoFiles, Videos


def video_detail(request, pk):
    template = 'videos/video_detail.html'
    video = get_object_or_404(Videos, pk=pk)
    video_file = get_object_or_404(VideoFiles, pk=pk)
    mini_videos = Videos.objects.all()

    return render(
        request, template, {
            'video': video,
            'video_file': video_file,
            'mini_videos': mini_videos,
        },
    )
