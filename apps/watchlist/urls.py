from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ReviewList, WatchListGV,
                    WatchListDetailAV, ReviewDetail,
                    ReviewCreate, StreamPlatformVS,
                    UserReview)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    ##### about Contents #####
    path('',
         WatchListGV.as_view(),
         name='movie-list'),
    path('<int:pk>/',
         WatchListDetailAV.as_view(),
         name='movie-detail'),

    ##### about StreamPlatform #####
    path('',
         include(router.urls)),

    ##### about Review #####
    path('<int:pk>/reviews/create/',
         ReviewCreate.as_view(),
         name='review-create'),
    path('<int:pk>/reviews/',
         ReviewList.as_view(),
         name='review-list'),
    path('reviews/<int:pk>/',
         ReviewDetail.as_view(),
         name='review-detail'),

    path('user-reviews/',
         UserReview.as_view(),
         name='user-review-detail'),
]

# path('stream/', StreamPlatformListAV.as_view(), name='streamplatform-list'),
# path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(),
#      name='streamplatform-detail'),
# path('review/', ReviewList.as_view(), name='review-list'),
# path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
