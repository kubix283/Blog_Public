from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.ListUsersAPI.as_view(), name='api_users'),
    path('user/<int:pk>/', views.RetrieveUpdateDestroyUsersAPI.as_view(), name='detail_api_user'),
    
]