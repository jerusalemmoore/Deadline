from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField,Div,Column,Field,HTML
from crispy_forms.bootstrap import StrictButton
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from .validators import validate_username
from django.utils.translation import gettext as _
import logging
logger=logging.getLogger('myLogger')
from .models import User

# LAYOUT FIELDS IN COLUMNAR FASHION INSIDE CONTAINER
class FieldsLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Div(
            HTML('''
            {% if form.errors %}
            <strong>Please correct the following:</strong>
                {% for field in form %}
                    {% for error in field.errors %}
                        <div>*{{error|escape}}</div>
                    {% endfor %}
                {% endfor %}
                {% for error in form.non_field_errors %}
                    <div>*{{error|escape}}</div>
                {% endfor %}
            {% endif %}

            '''),
            css_class="error"
            ),
            HTML("""
            {% for field in form %}
            <div class="field">
                <div class="label">{{field.label}}:</div>
                {{field}}
            </div>
            {% endfor %}
            """),
        )
class RegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =[ 'username', 'email', 'password1','password2']
    username = forms.CharField(
        required = True,
        widget=forms.TextInput(attrs={'class' : 'input'})
    )
    email = forms.EmailField(
        required = True,
        widget=forms.TextInput(attrs={'class' : 'input'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'input'}),
        label= "Password",
        required = True,
    )
    password2= forms.CharField(
        required = True,
        label = "Confirm Password",
        widget=forms.PasswordInput(attrs={'class' : 'input'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Div(
                HTML('<h1>REGISTER</h1>'),
                Div(
                    FieldsLayout(),
                    css_class="col"
                ),
                Submit('submit', 'Submit', css_class="btn btn-success"),
                css_class="container",
                css_id="register"
            )
        )
    # REGISTRATION VALIDATION
    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password1')
        confirmpassword = cleaned_data.get('password2')
        validate_username(username)
        validate_email(email)
        validate_password(password)
        if User.objects.filter(email=email).exists():
            raise ValidationError(
            _("Account with email address %(email)s already exists"), params={'email':email})
        if password != confirmpassword:
            raise ValidationError(
                _("Error, passwords don't match")
            )
        return cleaned_data

class UserLoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['email', 'password']
    id = forms.CharField(
        label = "Username/Email",
        required = True,
        widget=forms.TextInput(attrs={'class' : 'input'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class' : 'input'}),
        required = True,
    )

    # USERLOGIN LAYOUT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_errors = False
        self.helper.layout = Layout(
            Div(
                HTML('<h1>LOGIN</h1>'),
                Div(
                    FieldsLayout(),
                    css_class="col"
                ),
                Submit('submit', 'Submit', css_class="btn btn-success"),
                css_class="container",
                css_id="formwrapper"
            )
        )


    def clean(self):
        cleaned_data = super().clean()
        # id can either be EMAIL or USERNAME
        id = cleaned_data.get('id')
        password = cleaned_data.get('password')
        logger.error(id)
        logger.error(password)
        user1 = authenticate(email=id, password=password)
        logger.error(user1)
        logger.error(id)
        user2 = authenticate(username=id, password=password)
        logger.error(user2)

        if (user1 is None) and (user2 is None):
            raise ValidationError(
                _("Error, invalid username/password combination")
            )
        return cleaned_data


class EmailForm(forms.Form):
    subject = forms.CharField(
    widget=forms.TextInput(attrs={'class':'input'}),
    max_length=100, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'input','rows':4, 'cols':40}))

# EMAIL LAYOUT
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.form_show_errors = False

        self.helper.layout = Layout(
            Div(
                HTML('<h1>CONTACT</h1>'),
                Div(
                    Div(
                        HTML('{{formDescription}}'),
                        css_class="description"
                    ),
                    FieldsLayout(),
                    css_class="col"
                ),
            Submit('submit', 'Submit', css_class="btn btn-success"),
            css_class="container",
            css_id="contact",
            ),
        )
