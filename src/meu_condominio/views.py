from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm
from .models import Cond

def index(request):
	return render(request, 'meu_condominio/index.html')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		user = authenticate(username=request.POST['nome'],
							password=request.POST['password']
							)

		if form.is_valid() and user is not None:
			return HttpResponse('Em construcao')
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
			u.save()
			c = Cond(nome_condominio=request.POST['nome_condominio'],
					 nro_apartamentos=int(request.POST['nro_apartamentos']),
					 cep=request.POST['cep']
					)
			c.save()
			return HttpResponseRedirect(reverse('mc-login'))
	else:
		form = SignupForm()

	return render(request, 'meu_condominio/signup.html', {'form' : form})
