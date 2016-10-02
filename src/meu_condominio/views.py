from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm, UpdateForm
from .models import Condominio

def index(request):
  return render(request, 'meu_condominio/index.html')

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    user = authenticate(username=request.POST['nome'],
                        password=request.POST['password']
                        )

    if form.is_valid() and user is not None:
      if user.is_superuser == False:
        form = UpdateForm()
        return HttpResponseRedirect(reverse('mc-update'))
      else:
        auth_login(request, user)
        return render(request, 'meu_condominio/home.html',
                      {'nome' : user.username})
    else:
      messages.warning(request, 'Nome e/ou senha incorretos!')
  else:
    form = LoginForm()

  return render(request, 'meu_condominio/login.html', {'form' : form})

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      u = User.objects.create_user(request.POST['nome'],
                                   request.POST['email'],
                                   request.POST['senha']
                                   )
      u.is_superuser = True
      u.save()
      c = Condominio(nome_condominio=request.POST['nome_condominio'],
                    nro_apartamentos=int(request.POST['nro_apartamentos']),
                    cep=request.POST['cep']
                    )
      c.save()
      messages.success(request, 'Cadastro realizado com sucesso!')
      return HttpResponseRedirect(reverse('mc-login'))
  else:
    form = SignupForm()

  return render(request, 'meu_condominio/signup.html', {'form' : form})

def update(request, id):
  if request.method == 'POST':
    form = UpdateForm(request.POST)

    if form.is_valid():
      user = User.objects.get(pk=id)
      user.set_password(request.POST['password'])
      user.save()
      user = authenticate(username=user.username,
                          password=user.password
                          )
      auth_login(request, user)
      return HttpResponseRedirect(reverse('mc-home'))
  else:
    form = UpdateForm()

  return render(request, 'meu_condominio/update.html', {'form' : form})

def home(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/home.html',
                  {'nome' : request.user.username})
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse('mc-index'))

def financas(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/financas.html')
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def espacos(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/espacos.html')
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def funcionarios(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/funcionarios.html')
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def f_add(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/funcionarios/f_add.html')
  else:
    return HttpResponseRedirect(reverse('mc-login'))