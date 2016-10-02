# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-02 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_condominio', '0004_auto_20160909_0334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
