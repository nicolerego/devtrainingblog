# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150423_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designpost',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/blog/images', blank=True),
        ),
    ]
