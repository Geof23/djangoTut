# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('base', '0004_auto_20161216_0147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedb',
            fields=[
                ('auth', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
