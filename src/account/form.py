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
        if self.is_valid():

            email = self.clean_data['email']
            password = self.clean_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('login erroneo')




class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = Accountfields = ('email', 'username')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                account = Account.object.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
        raise forms.ValidationError("email '%s' esta en uso." % account.email)
    

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                account = Account.object.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
        raise forms.ValidationError("usuario '%s' esta en uso." % account.username)




