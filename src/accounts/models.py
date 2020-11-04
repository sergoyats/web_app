from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nickname = models.CharField(max_length=80, blank=True)

    @property
    def age(self):
        if self.birth_date:
            age = int((datetime.now().date() - self.birth_date).days / 365.25)
        else:
            age = 'No matter'
        return age


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, nickname=instance.email)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Following(models.Model):
    profile_id = models.ForeignKey(Profile, related_name="following", on_delete=models.CASCADE)
    following_profile_id = models.ForeignKey(Profile, related_name="followers", on_delete=models.CASCADE)

    # You can even add info about when user started following
    created = models.DateTimeField(auto_now_add=True)
