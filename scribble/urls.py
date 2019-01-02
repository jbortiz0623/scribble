# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
	path('', views.post_list, name='post_list'),
    # path('<int:pk>/post_details/', views.post_detail, name='post_detail'),
    path('post/create', views.post_create, name='post_create'),
    # path('<int:pk>/post_edit/', views.post_edit, name='post_edit'),
    # path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('comments', views.comment_list, name='comment_list'),
    # path('post',views.)
]
