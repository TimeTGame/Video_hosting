__all__ = []

from django.shortcuts import render
from videos.models import Videos


def index_render(request):
    template = 'homepage/index.html'
    videos = Videos.objects.all()

    return render(request, template, {'videos': videos})
