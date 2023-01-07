from django.urls import path, include

urlpatterns = [
    # path('users/', include('apps.user.urls'), name='users'),
    path('watch/', include('apps.watchlist.urls'), name='watch'),
    path('account/', include('apps.user.urls'), name='user')
]
