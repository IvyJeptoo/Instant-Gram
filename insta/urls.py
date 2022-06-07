from django.urls import path
from . import views


urlpatterns=[
    path('',views.sign_up,name = 'index'),
    path('home', views.index),
    path('signup', views.sign_up),    
    path('profile/<str:username>/',views.profile,name='profile'),
    path('edit/profile/',views.update_profile,name='update'),
    path('image/',views.post,name='post'),
    path('search/', views.search_profile, name='search'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('image/<id>', views.comment, name='comment'),
    path('like/<id>', views.like_post,name='like'),
    
]
