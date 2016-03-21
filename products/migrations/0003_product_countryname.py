# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_countrycode'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='countryName',
            field=models.TextField(null=True, blank=True),
        ),
    ]
