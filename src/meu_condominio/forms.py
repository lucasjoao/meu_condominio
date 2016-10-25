# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
  nome = forms.CharField(label='Seu nome:',
                         widget=forms.TextInput(
                         attrs={'placeholder':'Nome'}
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

class UpdateForm(forms.Form):
  password = forms.CharField(label='Sua nova senha', min_length=8,
                             widget=forms.PasswordInput(
                             attrs={'placeholder':'Senha'}
                             ))

class FuncionarioForm(forms.Form):
  nome = forms.CharField(label='Nome do funcionário:',
                         widget=forms.TextInput(attrs={'placeholder':'Nome'}))
  salario = forms.DecimalField(label='Salário do funcionário:',
                               widget=forms.TextInput(attrs={
                                      'placeholder':'Salário'}))

class MoradorForm(forms.Form):
  nome = forms.CharField(label='Nome do morador:',
    widget=forms.TextInput(attrs={'placeholder':'Nome'}))
  email = forms.EmailField(label='E-mail do morador:',
    widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
  moradores = forms.IntegerField(label='Quantos dependentes o morador possui:',
    widget=forms.TextInput(attrs={'placeholder':'Número de dependentes'}))
  numero_ape = forms.IntegerField(label='Número do apartamento do morador:',
    widget=forms.TextInput(attrs={'placeholder':'Número'}))

class RelatorioForm(forms.Form):
  placeholder = 'O dia é indiferente, mas preencha no formato dd/mm/aaaa'
  data = forms.DateField(label='Mês da competência:',
                         widget=forms.DateInput(
                          format='%d/%m/%Y',
                          attrs={'placeholder'=placeholder}
                          ))
