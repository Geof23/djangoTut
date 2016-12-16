# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regs',
            fields=[
                ('auth', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('fname', models.CharField(max_length=20, verbose_name=b'first name')),
                ('lname', models.CharField(max_length=20, verbose_name=b'last name')),
                ('institution', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15, verbose_name=b'Phone number')),
                ('program', models.CharField(default=b'si2', max_length=6, choices=[(b'si2', b'SI2'), (b'eager', b'EAGER'), (b'rapid', b'RAPID'), (b'voss', b'VOSS'), (b'career', b'CAREER')])),
                ('ptitle', models.CharField(max_length=100, verbose_name=b'program title')),
                ('nsfnum', models.CharField(max_length=20, verbose_name=b'nsf number')),
                ('adate', models.DateField(verbose_name=b'arrival date', blank=True)),
                ('ddate', models.DateField(verbose_name=b'departure date', blank=True)),
                ('airport', models.CharField(max_length=3, blank=True)),
                ('parkathotel', models.BooleanField(verbose_name=b'park at the hotel')),
                ('vegan', models.BooleanField()),
                ('vegetarian', models.BooleanField()),
                ('glutenfree', models.BooleanField(verbose_name=b'gluten free')),
                ('glutenallergy', models.BooleanField(verbose_name=b'gluten allergy')),
                ('kosher', models.BooleanField()),
                ('halal', models.BooleanField()),
                ('allergy', models.CharField(max_length=100, verbose_name=b'list allergies', blank=True)),
                ('other', models.CharField(max_length=100, verbose_name=b'other relevant info', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
