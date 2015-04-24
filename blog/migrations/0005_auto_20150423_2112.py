# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150423_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='codepost',
            name='status',
            field=models.TextField(default=b'unpublished', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='designpost',
            name='status',
            field=models.TextField(default=b'unpublished', editable=False),
            preserve_default=True,
        ),
    ]
