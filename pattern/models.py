from django.db import models
from user.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

class Pattern(models.Model):
    pattern_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default="description")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patterncreator")
    featured_image = CloudinaryField('image', default='placeholder')
    needle_size = models.CharField(max_length=100)
    gauge = models.CharField(max_length=100)
    yarn = models.CharField(max_length=100, default="yarn")
    difficulity_level = models.IntegerField(choices=LEVEL,)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"{self.pattern_name} | by {self.created_by}"