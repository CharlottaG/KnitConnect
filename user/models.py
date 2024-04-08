from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractUser, Group, Permission

LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.CharField(max_length=200, null=True, blank=True, unique=False,
                           default="Write some words about yourself.")
    profile_picture = CloudinaryField('image')
    difficulity_level = models.IntegerField(choices=LEVEL,default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Specify custom related_name arguments to avoid clashes
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Profile for {self.username}"