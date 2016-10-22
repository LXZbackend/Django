# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bittle', models.CharField(max_length=10)),
                ('bpub_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HerInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField()),
                ('Hcontent', models.CharField(max_length=1000)),
                ('hBook', models.ForeignKey(to='demo.BookInfo')),
            ],
        ),
    ]
