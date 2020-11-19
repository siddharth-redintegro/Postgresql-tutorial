from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name="hello_world"),
    path('users',views.users_list, name='users_list'),
    path('blogs',views.blog_list, name='blog_list'),
    path('insert', views.insert_blog, name='insert_blog'),
    path('delete', views.delete_blog, name='delete_blog'),
    path('update', views.update_blog, name='update_blog')

    path('new-user', views.insert_new_user, name="insert_user"),
    path('update-user/<int:id>',views.update_user, name="update_user"),
    path('delete-user/<int:id>',views.delete_user, name="delete_user"),
    path('all-users',views.user_list, name="user_list"),
]