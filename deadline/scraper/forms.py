from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField,Div,Column,Field
from crispy_forms.bootstrap import StrictButton
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
class RegistrationFrom(forms.Form):
        name = forms.CharField(
            label = "Name",
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
        confirmpassword = forms.EmailField(
            required = True,
            widget=forms.PasswordInput(attrs={'class' : 'input'}),
        )
