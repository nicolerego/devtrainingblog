# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150422_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designpost',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'static/blog', blank=True),
        ),
    ]
