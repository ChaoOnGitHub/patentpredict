# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-19 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patent_home', '0003_auto_20170819_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatentClaimText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_id', models.CharField(max_length=200)),
                ('claim', models.TextField()),
                ('sim_patent', models.TextField()),
                ('run_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Patent_Claim',
        ),
    ]