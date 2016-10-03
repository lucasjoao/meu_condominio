# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from .forms import *
from .models import Condominio, Funcionario, Apartamento

def index(request):
  return render(request, 'meu_condominio/index.html')

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    user = authenticate(username=request.POST['nome'],
                        password=request.POST['password']
                        )

    if form.is_valid() and user is not None:
      if user.is_superuser == False and user.last_login is None:
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
                    cep=request.POST['cep'],
                    user=u
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
    funcionarios = Funcionario.objects.all()
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

def moradores(request):
  if request.user.is_authenticated:
    return render(request, 'meu_condominio/moradores.html')
  else:
    return HttpResponseRedirect(reverse('mc-login'))

def m_add(request):
  if request.user.is_authenticated:
    c = Condominio.objects.get(user__pk=request.user.pk)
    count_a = Apartamento.objects.all().count()

    if request.method == 'POST':
      form = MoradorForm(request.POST)

      numero_ape = request.POST['numero_ape']
      existe_a = Apartamento.objects.filter(numero=numero_ape).exists()

      if form.is_valid() and count_a < c.nro_apartamentos and not existe_a:
        m = User.objects.create_user(request.POST['nome'],
                                     request.POST['email'],
                                     request.POST['email']
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
    moradores = User.objects.all().filter(is_superuser=False)
    return render(request, 'meu_condominio/moradores/m_view.html',
                  {'moradores' : moradores})
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
