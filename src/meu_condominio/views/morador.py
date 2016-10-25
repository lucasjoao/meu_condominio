# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from meu_condominio.forms import *
from meu_condominio.models import Condominio, Apartamento

def moradores(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/moradores.html',
                  {'user' : request.user})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def m_add(request):
  if request.user.is_authenticated:
    c = Condominio.objects.get(user__pk=request.user.pk)
    count_a = Apartamento.objects.all().filter(condominio__pk=c.pk).count()

    if request.method == 'POST':
      form = MoradorForm(request.POST)

      numero_ape = request.POST['numero_ape']
      existe_a = Apartamento.objects.filter(numero=numero_ape).filter(condominio__pk=c.pk).exists()

      if form.is_valid() and count_a < c.nro_apartamentos and not existe_a:
        m = User.objects.create_user(request.POST['nome'],
                                     request.POST['email'],
                                     'senhadefault'
                                     )
        m.save()

        a = Apartamento(numero=request.POST['numero_ape'], ocupado=True,
                    quantidade_moradores=str(int(request.POST['moradores'])+1),
                    condominio=c, user=m)
        a.save()

        messages.success(request, 'Morador adicionado com sucesso!')
        return HttpResponseRedirect(reverse('mc-m_view'))
      else:
        mensagem_tmp = 'Não há mais espaço no condominio e/ou '
        mensagem = mensagem_tmp + ' apartamento já está ocupado!'
        messages.warning(request, mensagem)
    else:
      form = MoradorForm()

    title = 'Cadastrar'
    m_min = count_a + 1
    m_max = c.nro_apartamentos
    replace = 'Valor entre 1 e ' + str(c.nro_apartamentos)
    form.fields['numero_ape'].widget.attrs['placeholder'] = replace

    return render(request, 'meu_condominio/moradores/form.html',
                {'form' : form, 'title' : title, 'm_min':m_min, 'm_max':m_max})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def m_view(request):
  if request.user.is_authenticated:
    c = Condominio.objects.get(user__pk=request.user.pk)
    apartamentos = Apartamento.objects.all().filter(condominio__pk=c.pk)
    return render(request, 'meu_condominio/moradores/m_view.html',
                  {'apartamentos' : apartamentos})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def m_del(request, id):
  if request.user.is_authenticated:
    morador = User.objects.get(pk=id)
    morador.delete()
    messages.success(request, 'Morador deletado com sucesso!')
    return HttpResponseRedirect(reverse('mc-m_view'))
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def m_edit(request, id):
  if request.user.is_authenticated:
    morador = User.objects.get(pk=id)
    apartamento = Apartamento.objects.get(user__pk=id)

    if request.method == 'POST':
      form = MoradorForm(request.POST)

      if form.is_valid():
        morador.username = request.POST['nome']
        morador.email = request.POST['email']
        morador.save()
        apartamento.quantidade_moradores = int(request.POST['moradores'])+1
        apartamento.save()
        messages.success(request, 'Morador editado com sucesso!')
        return HttpResponseRedirect(reverse('mc-m_view'))
    else:
      form = MoradorForm()

    form.fields['nome'].widget.attrs['placeholder'] = morador.username
    form.fields['email'].widget.attrs['placeholder'] = morador.email
    mensagem = 'VALOR NÃO FARÁ EFEITO!'
    form.fields['numero_ape'].widget.attrs['placeholder'] = mensagem
    form.fields['moradores'].widget.attrs['placeholder'] = apartamento.quantidade_moradores - 1
    title = 'Editar'
    return render(request, 'meu_condominio/moradores/form.html',
                  {'form' : form, 'title' : title})
  else:
    return HttpResponseRedirect(reverse('mc-login'))
