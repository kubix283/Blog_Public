from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.ListUsersAPI.as_view(), name='api_users'),
    path('user/<int:pk>/', views.RetrieveUpdateDestroyUsersAPI.as_view(), name='detail_api_user'),
    path('posts/', views.ListPostAPI.as_view(), name='api_posts'),
    path('post/<int:pk>/', views.RetrieveUpdatePostAPI.as_view(), name='api_detail_post'),
    path('post/<int:pk>/delete/', views.DestroyPostAPI.as_view(), name='api_delete_post'),
    
]