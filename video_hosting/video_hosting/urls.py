from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('users/', include('users.urls', namespace='users')),
    path('videos/', include('videos.urls', namespace='videos')),
    path('actions/', include('actions.urls', namespace='actions')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT,
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
