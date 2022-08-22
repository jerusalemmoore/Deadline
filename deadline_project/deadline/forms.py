from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField,Div,Column,Field
from crispy_forms.bootstrap import StrictButton
from .models import User
from django.core.exceptions import ValidationError
class LoginForm(forms.Form):
    username = forms.CharField(
        # label = "username",
        required = True,
        widget=forms.TextInput(attrs={'class' : 'input'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'input'}),
        required = True,
    )

class RegistrationForm(forms.Form):
        username = forms.CharField(
            required = True,
            widget=forms.TextInput(attrs={'class' : 'input'}),
        )
        email = forms.EmailField(
            required = True,
            widget=forms.TextInput(attrs={'class' : 'input'})
        )
        password = forms.CharField(
            widget=forms.PasswordInput(attrs={'class' : 'input'}),
            required = True,
        )
        confirmpassword = forms.CharField(
            required = True,
            label = "Confirm Password",
            widget=forms.PasswordInput(attrs={'class' : 'input'}),
        )
class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    username = forms.CharField(
            # label = "username",
        required = True,
        widget=forms.TextInput(attrs={'class' : 'input'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'input'}),
        required = True,
    )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError(
                "Error, invalid username/password combination"
            )
class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
