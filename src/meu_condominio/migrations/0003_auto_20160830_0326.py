# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 03:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meu_condominio', '0002_auto_20160830_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='morador',
            name='user',
        ),
        migrations.DeleteModel(
            name='Morador',
        ),
    ]