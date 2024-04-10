from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from .models import User

@receiver(user_signed_up)
def create_user_profile(sender, request, user, **kwargs):
    User.objects.create(username=user.username, userprofile=user.username)