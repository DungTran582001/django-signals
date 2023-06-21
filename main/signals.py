from django.core.signals import request_started
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, majority="IT")
        print("Profile created")
        

@receiver(post_save, sender=User)
def update_profile(sender, created, instance, *args, **kwargs):
    if not created:
        Profile.objects.filter(user=instance).update(majority="Changed")
        print("Profile updated")