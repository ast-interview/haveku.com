# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vedios', '0005_auto_20141221_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedio',
            name='thumbnail',
            field=models.URLField(blank=True, editable=False, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='vedio',
            name='vid',
            field=models.CharField(blank=True, null=True, max_length=300),
            preserve_default=True,
        ),
    ]
