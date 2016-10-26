# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from meu_condominio.forms import *
from meu_condominio.models import *

from datetime import datetime

def financas(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      option = 'Relatórios gerais'
    else:
      option = 'Relatórios'

    return render(request, 'meu_condominio/financas.html',
                  {'user' : request.user, 'option' : option})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def fin_add(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = RelatorioForm(request.POST)

      data_formatada = helper_data(request.POST['data'])

      existe_rel = Relatorio.objects.filter(data=data_formatada).exists()
      if form.is_valid and not existe_rel:
        # necessary things
        c = Condominio.objects.get(user__pk=request.user.pk)
        nro = Apartamento.objects.all().filter(condominio__pk=c.pk).count()

        # calculate balanco
        funcionarios = Funcionario.objects.all().filter(condominio__pk=c.pk)
        prejuizo = 0
        for funcionario in funcionarios:
          prejuizo += funcionario.salario
        lucro = nro * float(request.POST['condominio_taxa'])
        valor_balanco = lucro - prejuizo

        # calculate parcela
        todos_gastos = float(request.POST['agua']) + float(request.POST['luz']) + float(request.POST['gas']) + float(request.POST['manutencoes'])
        extra_valor_tmp = request.POST['extra_valor']
        todos_gastos += 0 if extra_valor_tmp == '' else float(extra_valor_tmp)
        gasto_por_apartamento = 0 if nro == 0 else todos_gastos/nro
        valor_parcela = float(request.POST['condominio_taxa']) + gasto_por_apartamento

        # save despesa_extra
        d = DespesaExtra()
        if extra_valor_tmp != '':
          d = DespesaExtra(nome=request.POST['extra_nome'],
                          valor=request.POST['extra_valor'],
                          motivo=request.POST['extra_motivo'])
        d.save()

        # save general rel
        rel_general = Relatorio(condominio=c, data=data_formatada,
                        agua=request.POST['agua'], luz=request.POST['luz'],
                        gas=request.POST['gas'],
                        condominio_taxa=request.POST['condominio_taxa'],
                        manutencoes=request.POST['manutencoes'], eh_geral=True,
                        despesa_extra=d, balanco=valor_balanco, parcela=0.00
                      )
        rel_general.save()

        # save individual rel
        if nro != 0:
          rel_ind = Relatorio(condominio=c, data=data_formatada,
                        agua=helper_rel_ind(request.POST['agua'], nro),
                        luz=helper_rel_ind(request.POST['luz'], nro),
                        gas=helper_rel_ind(request.POST['gas'], nro),
                        condominio_taxa=
                          helper_rel_ind(request.POST['condominio_taxa'], nro),
                        manutencoes=         helper_rel_ind(request.POST['manutencoes'], nro),
                        eh_geral=False, despesa_extra=d, balanco=0.00,
                        parcela=valor_parcela
                        )
          rel_ind.save()

        # finish
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
  if request.user.is_authenticated:
    c = Condominio.objects.get(user__pk=request.user.pk)

    if request.user.is_superuser:
      relatorios = Relatorio.objects.all().filter(condominio__pk=c.pk).filter(eh_geral=True)
    else:
      relatorios = Relatorio.objects.all().filter(condominio__pk=c.pk)

    return render(request, 'meu_condominio/financas/fin_view.html',
                  {'relatorios' : relatorios})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def fin_edit(request, id):
  pass

def fin_view_relatorio(request, id):
  pass

def helper_data(data):
  return data[3:]

def helper_rel_ind(valor, nro_moradores):
  return str(float(float(valor)/nro_moradores))