# authapp/urls.py

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    register, login, artist_only_view,
    manager_only_view, consumer_only_view
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('artist/', artist_only_view, name='artist_view'),
    path('manager/', manager_only_view, name='manager_view'),
    path('consumer/', consumer_only_view, name='consumer_view'),
]
