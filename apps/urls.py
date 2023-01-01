from django.urls import path, include

urlpatterns = [
    # path('users/', include('apps.user.urls'), name='users'),
    path('watchlist/', include('apps.watchlist.urls'), name='watchlist'),
]
