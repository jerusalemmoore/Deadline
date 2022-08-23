from django import forms
from django.contrib.auth import authenticate
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, MultiField,Div,Column,Field,HTML
from crispy_forms.bootstrap import StrictButton
from .models import User
from django.core.exceptions import ValidationError

# LAYOUT FIELDS IN COLUMNAR FASHION INSIDE CONTAINER
class FieldsLayout(Layout):
    def __init__(self, *args, **kwargs):
        super().__init__(
            Div(
            HTML('{{form.non_field_errors}}'),
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
        password = cleaned_data.get('password')
        confirmpassword = cleaned_data.get('confirmpassword')
        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(
            ("Username %(username)s already exists"), params={'username':username})
        if password != confirmpassword:
            raise ValidationError(
                ("Error, passwords don't match")
            )
        return cleaned_data

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
        cleaned_data = super(UserLoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError(
                "Error, invalid username/password combination"
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
                    FieldsLayout(),
                    css_class="col"
                ),
            Submit('submit', 'Submit', css_class="btn btn-success"),
            css_class="container",
            css_id="contact"
            )
        )
