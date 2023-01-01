from django.urls import path, include
from .views import StreamPlatformListAV, WatchListAV, WatchListDetailAV, StreamPlatformDetailAV

urlpatterns = [
    path('platforms/', StreamPlatformListAV.as_view(), name='platform-list'),
    path('platforms/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform-detail'),
    path('contents/', WatchListAV.as_view(), name='movie-list'),
    path('contents/<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
]
