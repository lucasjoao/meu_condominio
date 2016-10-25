# <controller>
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

from meu_condominio.forms import *

def financas(request):
  if request.user.is_authenticated:
    if request.user.is_superuser:
      option0 = 'Inserir dados'
    else:
      option0 = 'Relatório pessoal'

    option1 = 'Relatório geral'

    return render(request, 'meu_condominio/financas.html',
                  {'user' : request.user, 'option0' : option0,
                   'option1' : option1})
  else:
    return HttpResponseRedirect(reverse('mc-login'))
