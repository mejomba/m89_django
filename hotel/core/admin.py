from django.contrib import admin
from .models import User, Room, UserRoom

admin.site.register([User, Room, UserRoom])
