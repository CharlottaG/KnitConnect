from django.db import models
from user.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


LEVEL = ((0, "Beginner"), (1, "Intermediate"), (2, "Advanced"))

class Pattern(models.Model):
    pattern_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(default="description")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patterncreator")
    featured_image = CloudinaryField('image', default='https://res.cloudinary.com/dehwhmatn/image/upload/v1712673845/placeholder_pattern_y33fzt')
    needle_size = models.CharField(max_length=100)
    gauge = models.CharField(max_length=100)
    yarn = models.CharField(max_length=100, default="yarn")
    difficulity_level = models.IntegerField(choices=LEVEL,)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.pattern_name)
        super(Pattern, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.pattern_name} | by {self.created_by}"

       

class Comment(models.Model):
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"


