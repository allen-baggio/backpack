from django.db import models


class Request(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    buyer_username = models.CharField()
    provider_username = models.CharField()
    item = models.ForeignKey('Item')
    price = models.PositiveIntegerField(max_length=6)
    quantity = models.IntegerField(max_length=1)
    STATUS_ENUM = (
        'Ordered',
        'Confirmed',
        'Shipped',
        'Delivered',
        'Completed'
    )
    status = models.CharField(choices=STATUS_ENUM, default='Ordered')
    delivery_time = models.DateTimeField()
    created_time = models.DateTimeField()


class User(models.Model):
    phone = models.PositiveIntegerField(max_length=15)
    email = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=45)
    name = models.CharField(max_length=45)


class Session(models.Model):
    session_id = models.CharField(primary_key=True)
    username = models.EmailField()
    expired = models.DateTimeField()


class Item(models.Model):
    id = models.AutoField(max_length=10, primary_key=True)
    name = models.CharField(max_length=200)
    TYPE_ENUM = (
        'price_based',
        'availability_based'
    )
    type = models.CharField(choices=TYPE_ENUM)
    country = models.CharField(max_length=20)
    #link = models.CharField(max_length=50)
