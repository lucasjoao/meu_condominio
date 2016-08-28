from django import forms

class LoginForm(forms.Form):
	email = forms.EmailField(label='Seu e-mail:',
		                     widget=forms.TextInput(
		                     	attrs={'placeholder':'E-mail'}
		                     	)
		                     )
	password = forms.CharField(label='Sua senha', min_length=8,
						       widget=forms.PasswordInput(
								   attrs={'placeholder':'Senha'}
								   )
							   )