from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [

    # Post related links
    path('', views.ListPost.as_view(), name='list-posts'),
    path('<int:pk>/', views.DetailPost.as_view(), name='detail-post'),
    path('create-post/', views.CreatePost.as_view(), name='create-post'),
    path('update-post-<int:pk>/', views.UpdatePost.as_view(), name='update-post'),
    path('delete?<int:pk>/', views.DeletePost.as_view(), name='delete-post'),

    # Category related links
    path('category/<int:pk>', views.DetailCategory.as_view(), name='detail-category'),
    path('category/', views.ListCategory.as_view(), name='list-category'),
    path('create-category/', views.CreateCategory.as_view(), name='create-category'),
    path('update-category-<int:pk>/', views.UpdateCategory.as_view(), name='update-category'),
    path('delete?<int:pk>/', views.DeleteCategory.as_view(), name='delete-category'),
]
