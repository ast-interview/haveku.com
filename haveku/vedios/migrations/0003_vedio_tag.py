# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vedios', '0002_remove_vedio_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='vedio',
            name='tag',
            field=models.ForeignKey(default='', to='vedios.Tag'),
            preserve_default=True,
        ),
    ]
