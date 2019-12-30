from django.db.models.signals import post_save
from django.dispatch import receiver

from user.models import Profile, User


@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
