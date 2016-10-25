# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from meu_condominio.forms import *
from meu_condominio.models import Condominio, Funcionario


def funcionarios(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/funcionarios.html',
                  {'user' : request.user})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def f_add(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = FuncionarioForm(request.POST)

      if form.is_valid():
        c = Condominio.objects.get(user__pk=request.user.pk)
        f = Funcionario(nome=request.POST['nome'],
                        salario=request.POST['salario'],
                        condominio=c)
        f.save()
        messages.success(request, 'Funcionário adicionado com sucesso!')
        return HttpResponseRedirect(reverse('mc-f_view'))
    else:
      form = FuncionarioForm()

    title = 'Cadastrar'
    return render(request, 'meu_condominio/funcionarios/form.html',
                  {'form' : form, 'title' : title})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def f_view(request):
  if request.user.is_authenticated:
    c = Condominio.objects.get(user__pk=request.user.pk)
    funcionarios = Funcionario.objects.all().filter(condominio__pk=c.pk)
    return render(request, 'meu_condominio/funcionarios/f_view.html',
                  {'funcionarios' : funcionarios})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def f_del(request, id):
  if request.user.is_authenticated:
    funcionario = Funcionario.objects.get(pk=id)
    funcionario.delete()
    messages.success(request, 'Funcionário deletado com sucesso!')
    return HttpResponseRedirect(reverse('mc-f_view'))
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def f_edit(request, id):
  if request.user.is_authenticated:
    funcionario = Funcionario.objects.get(pk=id)

    if request.method == 'POST':
      form = FuncionarioForm(request.POST)

      if form.is_valid():
        funcionario.nome = request.POST['nome']
        funcionario.salario = request.POST['salario']
        funcionario.save()
        messages.success(request, 'Funcionário editado com sucesso!')
        return HttpResponseRedirect(reverse('mc-f_view'))
    else:
      form = FuncionarioForm()

    form.fields['nome'].widget.attrs['placeholder'] = funcionario.nome
    form.fields['salario'].widget.attrs['placeholder'] = funcionario.salario
    title = 'Editar'
    return render(request, 'meu_condominio/funcionarios/form.html',
                  {'form' : form, 'title' : title})
  else:
    return HttpResponseRedirect(reverse('mc-login'))
