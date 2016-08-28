from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'meu_condominio/index.html')

def login(request):
	return HttpResponse('login')

def signup(request):
	return HttpResponse('signup')