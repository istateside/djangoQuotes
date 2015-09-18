# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.ForeignKey(to='quotes.Source', blank=True),
        ),
    ]
