from django.db import models
from django.db.models.deletion import CASCADE


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone =models.CharField(max_length=200, null=True)
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
        ('indoor', 'Indoor'),
        ('Outdoor', 'Outdoor')
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS =(
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
    )
    status = models.CharField(max_length=200, choices = STATUS, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=CASCADE)
    category = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.customer} : {self.product}'



