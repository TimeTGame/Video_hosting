__all__ = []

from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import render


def index_render(request):
    template = 'homepage/index.html'

    return render(request, template)
