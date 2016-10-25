# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aparent', models.ForeignKey(blank=True, to='booktest.AreaInfo', null=True)),
            ],
            options={
                'db_table': 'areaInfo',
            },
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=10)),
                ('bpub_date', models.DateTimeField()),
                ('bread', models.IntegerField(default=0)),
                ('bcommet', models.IntegerField(default=0)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['id'],
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='HeroInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hname', models.CharField(max_length=10)),
                ('hgender', models.BooleanField()),
                ('Hcontent', models.CharField(max_length=1000)),
                ('isDelete', models.BooleanField(default=False)),
                ('hBook', models.ForeignKey(to='booktest.BookInfo')),
            ],
        ),
    ]
