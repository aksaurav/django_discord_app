# importing moduls
from django.forms import ModelForm
from .models import Room, Message, User
from django.contrib.auth.forms import UserCreationForm


# creating forms
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "password1", "password2"]


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participant"]


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]
