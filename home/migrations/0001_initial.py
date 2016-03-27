# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(max_length=10, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=64, choices=[(b'pb', b'price_based'), (b'ab', b'availability_based')])),
                ('country', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.AutoField(max_length=10, serialize=False, primary_key=True)),
                ('provider_username', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=20)),
                ('return_date', models.DateTimeField()),
                ('created_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('buyer_username', models.CharField(max_length=64)),
                ('provider_username', models.CharField(max_length=64)),
                ('price', models.PositiveIntegerField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(default=b'ordered', max_length=64, choices=[(b'ordered', b'Ordered'), (b'confirmed', b'Confirmed'), (b'shipped', b'Shipped'), (b'delivered', b'Delivered'), (b'completed', b'Completed'), (b'canceled', b'Canceled')])),
                ('delivery_time', models.DateTimeField()),
                ('created_time', models.DateTimeField()),
                ('item', models.ForeignKey(to='home.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.CharField(max_length=64, serialize=False, primary_key=True)),
                ('username', models.EmailField(max_length=254)),
                ('expired', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('phone', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=20, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
    ]
