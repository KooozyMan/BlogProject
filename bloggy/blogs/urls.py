from django.urls import path
from . import views


urlpatterns = [
   path('', views.main, name='main'),
   path('users/', views.users, name='users'),
   path('users/user/<int:id>', views.user, name='user'),
   path('categories/', views.categories, name='categories'),
   path('categories/category/<int:id>', views.category, name='category'),
   path('posts/', views.posts, name='posts'),
   path('posts/post/<int:id>', views.post, name='post'),
#    path('members/details/<int:id>', views.details, name='details'),
]