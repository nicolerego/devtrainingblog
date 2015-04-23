# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150423_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codepost',
            name='status',
            field=models.TextField(default=b'unpublished'),
        ),
        migrations.AlterField(
            model_name='designpost',
            name='status',
            field=models.TextField(default=b'unpublished'),
        ),
    ]
