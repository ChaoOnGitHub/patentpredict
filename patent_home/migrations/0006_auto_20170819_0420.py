# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-19 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent_home', '0005_auto_20170819_0410'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentClaim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_id', models.TextField()),
                ('claim', models.TextField()),
                ('sim_patent', models.TextField()),
                ('run_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='PatentClaimText',
        ),
    ]
