# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from meu_condominio.forms import *
from meu_condominio.models import Relatorio, Condominio, Apartamento

from datetime import datetime

def financas(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      option0 = 'Inserir dados'
    else:
      option0 = 'Relatório pessoal'

    option1 = 'Relatório geral'

    return render(request, 'meu_condominio/financas.html',
                  {'user' : request.user,
                   'option0' : option0, 'option1' : option1})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def fin_add(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = RelatorioForm(request.POST)

      data_formatada = helper_data(request.POST['data'])

      existe_rel = Relatorio.objects.filter(data=data_formatada).exists()
      if form.is_valid and not existe_rel:
        c = Condominio.objects.get(user__pk=request.user.pk)
        nro = Apartamento.objects.all().filter(condominio__pk=c.pk).count()

        # save general rel
        rel_general = Relatorio(condominio=c, data=data_formatada,
                        agua=request.POST['agua'], luz=request.POST['luz'],
                        gas=request.POST['gas'],
                        condominio_taxa=request.POST['condominio_taxa'],
                        manutencoes=request.POST['manutencoes'], eh_geral=True
                      )
        rel_general.save()

        # save individual rel
        rel_ind = Relatorio(condominio=c, data=data_formatada,
                        agua=helper_rel_ind(request.POST['agua'], nro),
                        luz=helper_rel_ind(request.POST['luz'], nro),
                        gas=helper_rel_ind(request.POST['gas'], nro),
                        condominio_taxa=
                          helper_rel_ind(request.POST['condominio_taxa'], nro),
                        manutencoes=
                          helper_rel_ind(request.POST['manutencoes'], nro),
                        eh_geral=False
                      )
        rel_ind.save()

        messages.success(request, 'Relatórios do mês adicionado com sucesso!')
        return HttpResponseRedirect(reverse('mc-fin_view'))
      else:
        mensagem = "Já há dados para esse mês!"
        messages.warning(request, mensagem)

    else:
      form = RelatorioForm()

    title = 'Cadastrar'

    return render(request, 'meu_condominio/financas/form.html',
      {'form' : form, 'title' : title})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def fin_view(request):
  pass

def fin_edit(request, id):
  pass

def fin_view_relatorio(request, id):
  pass

def helper_data(data):
  return data[3:]

def helper_rel_ind(valor, nro_moradores):
  return str(float(float(valor)/nro_moradores))