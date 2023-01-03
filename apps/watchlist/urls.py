from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ReviewList, StreamPlatformListAV, WatchListAV,
                    WatchListDetailAV, StreamPlatformDetailAV, ReviewDetail, ReviewCreate, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    ##### about Contents #####
    path('content/',
         WatchListAV.as_view(),
         name='movie-list'),
    path('content/<int:pk>/',
         WatchListDetailAV.as_view(),
         name='movie-detail'),

    ##### about StreamPlatform #####
    path('',
         include(router.urls)),

    ##### about Review #####
    path('content/<int:pk>/review-create',
         ReviewCreate.as_view(),
         name='review-create'),
    path('content/<int:pk>/review',
         ReviewList.as_view(),
         name='review-list'),
    path('content/review/<int:pk>',
         ReviewDetail.as_view(),
         name='review-detail'),
]

# path('stream/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
# path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
#      name='streamplatform-detail'),
# path('review/', ReviewList.as_view(), name='review-list'),
# path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
