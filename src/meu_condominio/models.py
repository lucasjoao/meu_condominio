from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class User(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.CharField(max_length=11)
	email = models.EmailField()
	senha = models.CharField(max_length=30)
	senha_default = models.BooleanField()
	admin = models.BooleanField()

	def __str__(self):
		return self.nome

@python_2_unicode_compatible
class Cond(models.Model):
	nome_condominio = models.CharField(max_length=100)
	nro_apartamentos = models.IntegerField()
	cep = models.CharField(max_length=8)

	def __str__(self):
		return self.nome_condominio
