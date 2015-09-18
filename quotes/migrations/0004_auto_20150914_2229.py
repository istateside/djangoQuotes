# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20150914_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='source',
            field=models.ForeignKey(blank=True, to='quotes.Source', null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='author',
            field=models.ForeignKey(blank=True, to='quotes.Author', null=True),
        ),
    ]
