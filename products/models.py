from django.db import models


class Country(models.Model):
    name = models.TextField(blank=True, null=True)
    imageUrl = models.URLField(blank=True, null=True)
    countryCode = models.TextField(blank=True, null=True)


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    imageUrl = models.URLField(blank=True, null=True)
    countryId = models.ForeignKey(Country, on_delete=models.CASCADE)
    countryName = models.TextField(blank=True, null=True)
    countryCode = models.TextField(blank=True, null=True)
    # active = models.BooleanField(default=True)
    # categories = models.ManyToManyField('Category', blank=True)
    # default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)
