from django.contrib import admin
from blog.models import Post, Category
from core.models import User

admin.site.register([Post, User, Category])
