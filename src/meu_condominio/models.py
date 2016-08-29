from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11)
	email = models.EmailField()
	senha = models.CharField(max_length=30)
	senha_default = models.BooleanField()
	admin = models.BooleanField()

class Cond(models.Model):
	nome_condominio = models.CharField(max_length=100)
	nro_apartamentos = models.IntegerField()
	cep = models.CharField(max_length=8)
