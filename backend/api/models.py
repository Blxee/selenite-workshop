from django.db import models
from django.utils import timezone

class Order(models.Model):
    """Represents an order from a buyer."""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
    buyer = models.CharField(max_length=64)
    product_type = models.ForeignKey(to='Product', on_delete=models.PROTECT)
    amount = models.PositiveIntegerField(null=True, blank=True)
    date_started = models.DateField(default=timezone.now, blank=True)
    date_due = models.DateField(null=True, blank=True)
    sell_price = models.PositiveIntegerField()


class Product(models.Model):
    """Represents a product type (sphere, spiral, soap bars..)."""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
    picture = models.ImageField()
    work_price = models.PositiveIntegerField()
