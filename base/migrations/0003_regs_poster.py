# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20161215_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='regs',
            name='poster',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
