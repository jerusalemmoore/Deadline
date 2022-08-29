from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User
import logging
logger=logging.getLogger('myLogger')
class SettingsBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            logger.error("authenticate:")
            user = User.objects.get(email=email)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
