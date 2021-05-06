from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from apps.carts.models import Cart
from .utils import randomString



class Delivery(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return self.name
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="orders", null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    order_id = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, related_name='orders', null=True)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0, null=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f"order {self.order_id}"

    
@receiver(pre_save, sender=Order)
def pre_save_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = randomString()

