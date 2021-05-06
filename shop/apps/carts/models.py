from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from apps.products.models import ProductItem


class Cart(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)    

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_item = models.ForeignKey(ProductItem, related_name='product_in_cart', on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1, blank=True)

    def __str__(self):
        return f"{self.cart.id} = cart items"

    

@receiver(post_save, sender=User)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
