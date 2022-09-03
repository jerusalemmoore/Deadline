from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import MinimumLengthValidator

from django.utils.translation import gettext as _
from .models import User

# my custom validator for username
    # check if username already exists in db
# def validate_username(username):
#     if User.objects.filter(username=username).exists():
#         raise ValidationError(
#             _('Account with username %(username)s already exists'),
#             params = {'username' : username}
#         )
