from django.urls import path
from .views import ListUsersAPI


urlpatterns = [
    path('', ListUsersAPI.as_view(), name='api_users'),
]