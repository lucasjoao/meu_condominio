from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, SignupForm

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
			return render(request, 'meu_condominio/index.html')
	else:
		form = SignupForm()

	return render(request, 'meu_condominio/signup.html', {'form' : form})
