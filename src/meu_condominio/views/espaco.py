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
    return render(request, 'meu_condominio/espacos.html',
                  {'user' : request.user})
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
        r = Reserva(condominio=c, dia=dia, turno=turno, user=request.user)
        r.save()

        # finish
        messages.success(request, 'Reserva adicionada com sucesso!')
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
