# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-29 01:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meu_condominio', '0004_auto_20161026_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=3)),
                ('turno', models.CharField(max_length=5)),
                ('apartamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_condominio.Apartamento')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meu_condominio.Condominio')),
            ],
        ),
    ]
