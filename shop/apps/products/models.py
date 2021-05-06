from django.db import models
from django.urls import reverse
from apps.categories.models import Category


PRODUCT_COLORS = (
    ('BLACK', 'Black'),
    ('BLUE', 'Blue'),
    ('RED', 'Red'),
    ('BROWN', 'Brown'),
    ('PURPLE', 'Purple'),
)


class Product(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name='product name')
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs = {"pk" : self.pk})


class InStockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(quantity=0)


class ProductItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()


class ProductItem(models.Model):
    color = models.CharField(choices=PRODUCT_COLORS, max_length=255, db_index=True, default=('PURPLE', 'Purple'))
    size = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # 2000.00
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_items')

    def __str__(self):
        return f"{self.product.name}'s item of color {self.color}"
    def get_absolute_url(self):
        return reverse('productitem-detail', kwargs = {'pk' : self.pk})
    
    objects = ProductItemManager()
    instock = InStockManager()

    def add_to_bookmark_url(self):
        return reverse('add-to-bookmark', kwargs = {'pk': self.pk})
    
    
    



class ProductItemImage(models.Model):
    image = models.ImageField(upload_to='productImages')
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='product_item_images')

    def __str__(self):
        return f"{self.product_item.product.name}'s image of {self.product_item.color} item"
