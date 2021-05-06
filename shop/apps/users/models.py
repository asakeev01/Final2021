from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from apps.products.models import ProductItem


class Bookmark(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_items = models.ManyToManyField(ProductItem, related_name='bookmarks')

    def __str__(self):
        return f"{self.user.username}'s bookmarks"
    

@receiver(post_save, sender=User)
def create_user_bookmark(sender, instance, created, **kwargs):
    if created:
        Bookmark.objects.create(user=instance)

