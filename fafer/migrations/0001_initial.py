# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=16)),
                ('mobile', models.CharField(max_length=11, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('ip', models.IPAddressField(null=True)),
                ('nickname', models.CharField(max_length=50, null=True)),
                ('signup_at', models.DateTimeField(null=True)),
                ('lastlogin', models.DateTimeField(null=True)),
            ],
        ),
    ]
