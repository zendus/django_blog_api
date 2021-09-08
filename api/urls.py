from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('all-posts/', views.all_posts, name='all_posts'),
    path('all-posts/<int:pk>/', views.get_post_by_id, name='post_by_id'),
    path('all-posts/<str:section>/', views.get_post_by_section, name='post_by_section'),
    path('create-post/', views.create_new_post, name='create_new_post'),
    path('update-post/<int:pk>', views.update_post, name='update_post'),
    path('delete-post/<int:pk>', views.delete_post, name='delete_post'),
    path('comments/<int:pk>', views.get_post_comments, name='post_comments'),
]