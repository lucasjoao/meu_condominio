from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import LoginForm, SignupForm
from .models import User, Cond

def index(request):
	return render(request, 'meu_condominio/index.html')

def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)

		if form.is_valid():
			return HttpResponse('Em construcao')
	else:
		form = LoginForm()

	return render(request, 'meu_condominio/login.html', {'form' : form})

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)

		if form.is_valid():
			u = User(nome=request.POST['nome'],
					 cpf=request.POST['cpf'],
					 email=request.POST['email'],
					 senha=request.POST['senha'],
					 senha_default=False,
					 admin=True
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
