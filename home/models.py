from django.db import models


class Request(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    buyer_username = models.CharField(max_length=64)
    provider_username = models.CharField(max_length=64)
    item = models.ForeignKey('Item')
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    STATUS_ENUM = (
        ('ordered', 'Ordered'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    )
    status = models.CharField(choices=STATUS_ENUM, default='ordered', max_length=64)
    delivery_time = models.DateTimeField()
    created_time = models.DateTimeField()


class User(models.Model):
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)


class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=64)
    username = models.EmailField()
    expired = models.DateTimeField()


class Item(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    TYPE_ENUM = (
        ('pb', 'price_based'),
        ('ab', 'availability_based')
    )
    type = models.CharField(choices=TYPE_ENUM, max_length=64)
    country = models.CharField(max_length=20)


class Itinerary(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    provider_username = models.CharField(max_length=64)
    country = models.CharField(max_length=20)
    return_date = models.DateTimeField()
    created_time = models.DateTimeField()

