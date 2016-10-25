# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

# código da classe do usuário padrão do django está em:
# https://github.com/django/django/blob/master/django/contrib/auth/models.py

@python_2_unicode_compatible
class Condominio(models.Model):
  nome_condominio = models.CharField(max_length=100)
  nro_apartamentos = models.IntegerField()
  cep = models.CharField(max_length=8)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def __str__(self):
    return self.nome_condominio

@python_2_unicode_compatible
class Funcionario(models.Model):
  nome = models.CharField(max_length=100)
  salario = models.DecimalField(max_digits=20, decimal_places=2)
  condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)

  def __str__(self):
    return self.nome

@python_2_unicode_compatible
class Apartamento(models.Model):
  numero = models.IntegerField()
  ocupado = models.BooleanField()
  quantidade_moradores = models.IntegerField()
  condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

  def __str__(self):
    return self.numero

class SingletonModel(models.Model):
  class Meta:
    abstract = True

  def save(self, *args, **kwargs):
    self.pk = 1
    super(SingletonModel, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    pass

  @classmethod
  def load(cls):
    obj, created = cls.objects.get_or_create(pk=1)
    return obj

class FaleConosco(SingletonModel):
  dev0_nome = models.CharField(max_length=100, default='Lucas João Martins')
  dev0_email = models.EmailField(default='lucasjoao.lj@gmail.com')
  dev1_nome = models.CharField(max_length=100, default='Wesley Mayk Gama Luz')
  dev1_email = models.EmailField(default='w_mayk007@hotmail.com')

@python_2_unicode_compatible
class Relatorio(models.Model):
  condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE)
  data = models.CharField(max_length=7)
  agua = models.DecimalField(max_digits=20, decimal_places=2)
  luz = models.DecimalField(max_digits=20, decimal_places=2)
  gas = models.DecimalField(max_digits=20, decimal_places=2)
  condominio_taxa = models.DecimalField(max_digits=20, decimal_places=2)
  manutencoes = models.DecimalField(max_digits=20, decimal_places=2)
  eh_geral = models.BooleanField()

  def __str__(self):
    return self.data
