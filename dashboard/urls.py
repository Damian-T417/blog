from django.urls import path

from . import views

app_name = 'admin'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('getaction', views.get_action, name='get_action'),

    path('posts/', views.Posts.as_view(), name='posts'),
    path('posts/nuevo/', views.new_post, name='new_post'),
    path('posts/editar/<int:id>/', views.edit_post, name='edit_post'),
    path('posts/<int:id>/', views.Posts.as_view(), name='delete_post'),

    path('tags/', views.Tags.as_view(), name='tags'),
    path('tags/nuevo', views.new_tag, name='new_tag'),
    path('tags/editar/<int:id>/', views.edit_tag, name='edit_tag'),
    path('tags/borrar/<int:id>/', views.delete_tag, name='delete_tag'),
]
