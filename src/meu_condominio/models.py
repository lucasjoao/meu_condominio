from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Condominio(models.Model):
	nome_condominio = models.CharField(max_length=100)
	nro_apartamentos = models.IntegerField()
	cep = models.CharField(max_length=8)

	def __str__(self):
		return self.nome_condominio

@python_2_unicode_compatible
class Funcionario(models.Model):
  nome = models.CharField(max_length=100)
  salario = models.DecimalField(max_digits=20, decimal_places=2)

  def __str__(self):
    return self.nome
