from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser

LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    bio = models.CharField(max_length=200, null=True, blank=True, unique=False,
                           default="Write some words about yourself.")
    profile_picture = CloudinaryField('image', default='https://res.cloudinary.com/dehwhmatn/image/upload/v1712673845/placeholder_palitb')
    difficulity_level = models.IntegerField(choices=LEVEL,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.username}"