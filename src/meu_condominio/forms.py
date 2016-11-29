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
  gasto_total = 'Gasto total'
  data = forms.DateField(label='Mês da competência:',
                         widget=forms.DateInput(
                          format='%d/%m/%Y',
                          attrs={'placeholder' : placeholder}
                          ))
  agua = forms.DecimalField(label=gasto_total + ' com água:',
    widget=forms.TextInput(attrs={'placeholder':gasto_total}))
  luz = forms.DecimalField(label=gasto_total + ' com luz:',
    widget=forms.TextInput(attrs={'placeholder':gasto_total}))
  gas = forms.DecimalField(label=gasto_total + ' com gás:',
    widget=forms.TextInput(attrs={'placeholder':gasto_total}))
  condominio_taxa = forms.DecimalField(label='Taxa de condomínio:',
    widget=forms.TextInput(attrs={'placeholder':'Valor por apartamento'}))
  manutencoes = forms.DecimalField(label=gasto_total + ' com manutenções:',
    widget=forms.TextInput(attrs={'placeholder':gasto_total}))
  extra_nome = forms.CharField(label='Nome da despesa extra:', required=False,
    widget=forms.TextInput(attrs={'placeholder':'Nome'}))
  extra_valor = forms.DecimalField(label='Valor da despesa extra:',
    required=False,
    widget=forms.TextInput(attrs={'placeholder':'Valor'}))
  extra_motivo = forms.CharField(label='Motivo da despesa extra:',
    required=False,
    widget=forms.TextInput(attrs={'placeholder':'Motivo'}))

class ReservaForm(forms.Form):
  label_dia = 'Dia da semana (preencha no formato adequado):'
  placeholder_dia = 'Dom, Seg, Ter, Qua, Qui, Sex ou Sab'
  dia = forms.CharField(label=label_dia,
    widget=forms.TextInput(attrs={'placeholder':placeholder_dia}))

  label_turno = 'Turno (preencha no formato adequado):'
  placeholder_turno = 'Manhã, Tarde ou Noite'
  turno = forms.CharField(label=label_turno,
    widget=forms.TextInput(attrs={'placeholder':placeholder_turno}))
