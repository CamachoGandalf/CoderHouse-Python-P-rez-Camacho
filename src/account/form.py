from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Requiere un mail valido")

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")
        



class AccountAuthenticationForm(forms.ModelsForm):

    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        email = self.clean_data['email']
        password = self.clean_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('login erroneo')






