# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fafer', '0002_auto_20151120_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
