from django.db import models


# from django.db.models.signals import post_save
# from django.utils.safestring import mark_safe
# from django.utils.text import slugify
# from django.core.urlresolvers import reverse

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    imageUrl = models.URLField(blank=True, null=True)
    countryName = models.TextField(blank=True, null=True)
    countryCode = models.TextField(blank=True, null=True)
    # active = models.BooleanField(default=True)
    # categories = models.ManyToManyField('Category', blank=True)
    # default = models.ForeignKey('Category', related_name='default_category', null=True, blank=True)

# objects = ProductManager()
#
# class Meta:
# 	ordering = ["-title"]
#
# def __unicode__(self): #def __str__(self):
# 	return self.title
#
# def get_absolute_url(self):
# 	return reverse("product_detail", kwargs={"pk": self.pk})
#
# def get_image_url(self):
# 	img = self.productimage_set.first()
# 	if img:
# 		return img.image.url
# 	return img #None
