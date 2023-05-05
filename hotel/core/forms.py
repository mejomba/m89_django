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


class CustomLoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())


class OtpForm(forms.Form):
    otp = forms.CharField(max_length=40)
