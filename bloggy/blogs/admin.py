from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from .models import Category

# admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
