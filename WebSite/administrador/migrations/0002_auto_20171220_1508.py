# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-20 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselimgs',
            name='img1',
            field=models.CharField(default='media/index_carousel/1.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='carouselimgs',
            name='img2',
            field=models.CharField(default='media/index_carousel/2.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='carouselimgs',
            name='img3',
            field=models.CharField(default='media/index_carousel/3.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='carouselimgs',
            name='img4',
            field=models.CharField(default='media/index_carousel/4.png', max_length=500),
        ),
        migrations.AlterField(
            model_name='carouselimgs',
            name='img5',
            field=models.CharField(default='media/index_carousel/5.png', max_length=500),
        ),
    ]