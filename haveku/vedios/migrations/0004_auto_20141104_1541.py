# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vedios', '0003_vedio_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vedio',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vedio',
            name='tag',
            field=models.ForeignKey(null=True, blank=True, to='vedios.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vedio',
            name='title',
            field=models.CharField(null=True, max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
