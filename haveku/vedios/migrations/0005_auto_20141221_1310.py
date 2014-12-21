# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vedios', '0004_auto_20141104_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.AddField(
            model_name='tag',
            name='catalogue',
            field=models.ForeignKey(to='vedios.Catalogue', blank=True, null=True),
            preserve_default=True,
        ),
    ]
