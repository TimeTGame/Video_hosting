from django.urls import path
import videos.views as views

app_name = 'videos'

urlpatterns = [
    path('<int:pk>/', views.video_detail, name='video_detail'),
]
