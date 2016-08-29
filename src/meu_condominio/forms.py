# coding: utf8
from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label='Seu e-mail:',
		                     widget=forms.TextInput(
		                     	attrs={'placeholder':'E-mail'}
		                     ))
	password = forms.CharField(label='Sua senha', min_length=8,
						       widget=forms.PasswordInput(
								   attrs={'placeholder':'Senha'}
								))

class SignupForm(forms.Form):
	nome = forms.CharField(label='Seu nome:',
						   widget=forms.TextInput(
						   		attrs={'placeholder':'Nome'}
							))
	cpf = forms.CharField(label='Seu CPF',
						  widget=forms.TextInput(
						   		attrs={'placeholder':'CPF'}
						  ))
	email = forms.EmailField(label='Seu e-mail:',
		                     widget=forms.TextInput(
		                     	attrs={'placeholder':'E-mail'}
		                     ))
	senha = forms.CharField(label='Sua senha:', min_length=8,
						   widget=forms.TextInput(
						   		attrs={'placeholder':'Senha'}
							))
	nome_condominio = forms.CharField(label='Nome do condomínio:',
								      widget=forms.TextInput(
									  	attrs={'placeholder':'Condomínio'}
									  ))
	nro_apartamentos = forms.IntegerField(label='Número de apartamentos:',
										  widget=forms.TextInput(
										  	attrs={'placeholder':'Quantidade'}
									  	  ))
	cep = forms.CharField(label='CEP:',
						   widget=forms.TextInput(
						   		attrs={'placeholder':'CEP'}
						  ))
