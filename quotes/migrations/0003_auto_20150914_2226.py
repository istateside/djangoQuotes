# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20150914_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='author',
            field=models.ForeignKey(to='quotes.Author', blank=True),
        ),
    ]
