from django.urls import path
import homepage.views as views

app_name = 'homepage'

urlpatterns = [
    path('', views.index_render, name='homepage'),
]
