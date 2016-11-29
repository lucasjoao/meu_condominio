# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User

from meu_condominio.forms import *
from meu_condominio.models import *

def espacos(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      c = Condominio.objects.get(user__pk=request.user.pk)
    else:
      a = Apartamento.objects.get(user__pk=request.user.pk)
      c = Condominio.objects.get(pk=a.condominio)

    manha = helper_table('Manhã', c.pk)
    tarde = helper_table('Tarde', c.pk)
    noite = helper_table('Noite', c.pk)

    return render(request, 'meu_condominio/espacos.html',
                  {'user' : request.user, 'manha' : manha, 'tarde' : tarde,
                   'noite' : noite})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def esp_res(request):
  if request.user.is_authenticated:
    if request.method == 'POST':
      form = ReservaForm(request.POST)

      turno = request.POST['turno']
      dia = request.POST['dia']

      a = Apartamento.objects.get(user__pk=request.user.pk)
      c = Condominio.objects.get(pk=a.condominio)
      existe_res = Reserva.objects.filter(dia=dia).filter(turno=turno).filter(condominio__pk=c.pk).exists()
      if form.is_valid and not existe_res:
        r = Reserva(condominio=c, dia=dia, turno=turno, apartamento=a)
        r.save()

        return HttpResponseRedirect(reverse('mc-espacos'))
      else:
        mensagem = "Já há uma reserva para esse dia e turno!"
        messages.warning(request, mensagem)

    else:
      form = ReservaForm()

    return render(request, 'meu_condominio/espacos/form.html',
      {'form' : form})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def esp_view(request):
  if request.user.is_authenticated:
    option = ''
    if request.user.is_superuser:
      c = Condominio.objects.get(user__pk=request.user.pk)
      reservas = Reserva.objects.all().filter(condominio__pk=c.pk)
    else:
      a = Apartamento.objects.get(user__pk=request.user.pk)
      reservas = Reserva.objects.all().filter(apartamento=a)

    return render(request, 'meu_condominio/espacos/esp_view.html',
                  {'user' : request.user, 'reservas' : reservas})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def esp_del(request, id):
  if request.user.is_authenticated:
    reserva = Reserva.objects.get(pk=id)
    reserva.delete()
    if request.user.is_superuser:
      messages.success(request, 'Reserva bloqueada com sucesso!')
    else:
      messages.success(request, 'Reserva cancelada com sucesso!')
    return HttpResponseRedirect(reverse('mc-e_view'))
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def helper_table(t, cond_pk):
  vector = [False] * 7
  for reserva in Reserva.objects.all().filter(turno=t).filter(condominio__pk=cond_pk):
    if reserva.dia == 'Dom':
      vector[0] = True
    elif reserva.dia == 'Seg':
      vector[1] = True
    elif reserva.dia == 'Ter':
      vector[2] = True
    elif reserva.dia == 'Qua':
      vector[3] = True
    elif reserva.dia == 'Qui':
      vector[4] = True
    elif reserva.dia == 'Sex':
      vector[5] = True
    elif reserva.dia == 'Sab':
      vector[6] = True
  return vector