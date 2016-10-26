# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-26 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_condominio', '0003_auto_20161026_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despesaextra',
            name='motivo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='despesaextra',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='despesaextra',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]