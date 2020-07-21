from django.urls import path

from . import views

app_name = 'home'
 
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('tag/<slug:slug>/', views.Home.as_view(), name='type'),
    path('post/<slug:slug>/', views.single_post, name='single_post'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
