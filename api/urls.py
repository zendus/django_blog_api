from django.urls import path
from knox import views as knox_views
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
    path('register/', views.RegisterUser.as_view(), name='register_user'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]