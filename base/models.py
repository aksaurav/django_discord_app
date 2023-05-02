from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


"""This room class will a table in the database"""


class Room(models.Model):
    """We need user to host the room"""

    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # the host should be unique, that's why we need a ForeignKey
    """the User model is a built-in model that provides basic authentication
    features such as user authentication,
    user creation, user management, password management, and more."""
    # user will host a room
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    # and the topic also needs to be unique
    # And that host can  have multiple topic
    name = models.CharField(max_length=200)
    # room has to have a name
    description = models.TextField(null=True, blank=True)  # this cannot be empty
    participant = models.ManyToManyField(User, related_name="paricipants", blank=True)
    # this will record the time for the first time only
    updated = models.DateTimeField(auto_now=True)
    # will take a snapshot every time
    # this will record the time everytime
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self) -> str:
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # CASCADE : if Room get's deleted all of the child class will delete as well
    body = models.TextField()  # empty because we want to force our user to have a msg
    updated = models.TimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    # string representation
    def __str__(self) -> str:
        return self.body[0:50]  # trim down to fifty characters
