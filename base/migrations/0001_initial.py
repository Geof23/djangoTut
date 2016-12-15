# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Regs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('institution', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('program', models.CharField(default='si2', max_length=6)),
                ('ptitle', models.CharField(max_length=100)),
                ('nsfnum', models.CharField(max_length=20)),
                ('adate', models.DateTimeField(blank=True, verbose_name='arrival date')),
                ('airport', models.CharField(blank=True, max_length=3)),
                ('parkathotel', models.BooleanField()),
                ('vegan', models.BooleanField()),
                ('vegetarian', models.BooleanField()),
                ('glutenfree', models.BooleanField()),
                ('glutenallergy', models.BooleanField()),
                ('kosher', models.BooleanField()),
                ('halal', models.BooleanField()),
                ('allergy', models.CharField(blank=True, max_length=100)),
                ('other', models.CharField(blank=True, max_length=100)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]