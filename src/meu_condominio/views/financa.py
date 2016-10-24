from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def financas(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/financas.html',
                  {'user' : request.user})
  else:
    return HttpResponseRedirect(reverse('mc-login'))
