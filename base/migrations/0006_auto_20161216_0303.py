# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_feedb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedb',
            old_name='body',
            new_name='Feedback_and_comments',
        ),
    ]
