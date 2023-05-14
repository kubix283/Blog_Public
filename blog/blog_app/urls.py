from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.comment_post, name='post_detail'),
    path('add-post/', views.create_post, name='post_create'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
]
