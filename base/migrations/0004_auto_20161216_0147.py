# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_regs_poster'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regs',
            old_name='adate',
            new_name='Arrival_date',
        ),
        migrations.RenameField(
            model_name='regs',
            old_name='ddate',
            new_name='Departure_date',
        ),
        migrations.RenameField(
            model_name='regs',
            old_name='phone',
            new_name='Phone',
        ),
        migrations.RenameField(
            model_name='regs',
            old_name='poster',
            new_name='Poster_URL',
        ),
        migrations.AlterField(
            model_name='regs',
            name='airport',
            field=models.CharField(max_length=3, verbose_name=b'Airport (if known)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regs',
            name='nsfnum',
            field=models.CharField(max_length=20, verbose_name=b'NSF Award Number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='regs',
            name='program',
            field=models.CharField(default=b'si2', max_length=6, verbose_name=b'Primary Funding Program', choices=[(b'si2', b'SI2'), (b'eager', b'EAGER'), (b'rapid', b'RAPID'), (b'voss', b'VOSS'), (b'career', b'CAREER')]),
            preserve_default=True,
        ),
    ]
