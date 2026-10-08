from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Category, Post, Comment

def main(request):
   template = loader.get_template('main.html')
   return HttpResponse(template.render())

def users(request):
   users = User.objects.all().values()
   template = loader.get_template('users.html')
   context = {
      'users' : users
   }

   return HttpResponse(template.render(context, request))

def user(request, id):
   user = User.objects.get(id=id)
   template = loader.get_template('user.html')
   context = {
      'user' : user
   }

   return HttpResponse(template.render(context, request))

def categories(request):
   categories = Category.objects.all().values()
   template = loader.get_template('categories.html')
   context = {
      'categories' : categories
   }

   return HttpResponse(template.render(context, request))

def category(request, id):
   category = Category.objects.get(id=id)
   template = loader.get_template('category.html')
   context = {
      'category' : category
   }

   return HttpResponse(template.render(context, request))

def posts(request):
   posts = Post.objects.select_related().all()
   template = loader.get_template('posts.html')
   context = {
      'posts': posts
   }

   return HttpResponse(template.render(context, request))

def post(request, id):
   post = Post.objects.select_related().get(id=id)
   comments = Comment.objects.filter(post_id=id)
   template = loader.get_template('post.html')
   context = {
      'post' : post,
      'comments': comments,
   }

   return HttpResponse(template.render(context, request))
