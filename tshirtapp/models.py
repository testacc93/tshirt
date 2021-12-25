from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

class Tshirt(models.Model):
    tshirtid = models.CharField(default="T1", unique=True, max_length=64)
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=10)
    price = models.IntegerField()
    colour = models.CharField(max_length=64)

    def __str__(self):
        return self.tshirtid

class Customer(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    address = models.CharField(max_length=1000)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    orderid = models.CharField(max_length=64)
    customer = models.CharField(max_length=64)
    tshirt = models.ForeignKey(Tshirt, default=1, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.orderid




