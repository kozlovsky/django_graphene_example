from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    picture = models.ImageField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class CartItem(models.Model):
    quantity = models.IntegerField(default=1)
    customer = models.ForeignKey(Customer, related_name='cart_items')
    product = models.ForeignKey(Product, related_name='cart_items')

    class Meta:
        unique_together = (('customer', 'product'),)

    def __str__(self):
        return u'%s x %d' % (self.product, self.quantity)

@python_2_unicode_compatible
class Order(models.Model):
    CREATED = 'CREATED'
    SHIPPED = 'SHIPPED'
    DELIVERED = 'DELIVERED'
    CANCELLED = 'CANCELLED'

    STATUS_CHOICES = (
        (CREATED, 'CREATED'),
        (SHIPPED, 'SHIPPED'),
        (DELIVERED, 'DELIVERED'),
        (CANCELLED, 'CANCELLED'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CREATED)
    date_created = models.DateField(auto_now_add=True)
    date_shipped = models.DateField(blank=True, null=True)
    date_delivered = models.DateField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, related_name='orders')

    def __str__(self):
        return u'Order#%d' % self.id

@python_2_unicode_compatible
class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')

    class Meta:
        unique_together = (('order', 'product'),)

    def __str__(self):
        return u'%s: %s x %d' % (self.order, self.product, self.quantity)
