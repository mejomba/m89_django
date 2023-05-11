from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm


# class CustomUserAdmin(UserAdmin):
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("email", "username", 'is_author')
    list_filter = ('is_author', 'is_customer')
    # search_fields = ('username', 'email')


admin.site.register(User, CustomUserAdmin)
