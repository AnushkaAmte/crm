from os import name
from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ("Indoor", "Indoor"),
        ("Outdoor", "Outdoor"),
    )
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True, choices=CATEGORY)
    description = models.CharField(max_length=100, null=True)
    price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
# m-n for order&product
# 1-n for customer&order
# 1-n for product&customer


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out For Delivery', 'Out For Delivery'),
        ('Delivered', 'Delivered')
    )

    status = models.CharField(max_length=50, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    note = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.product.name
