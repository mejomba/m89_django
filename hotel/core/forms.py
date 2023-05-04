from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Room


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")


class ReserveRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
