from django.db.models.signals import post_save
from django.dispatch import receiver

from book.models import Book, BookMeta


@receiver(post_save, sender=Book)
def book_post_save(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'bookmeta'):
        BookMeta.objects.create(book=instance)
