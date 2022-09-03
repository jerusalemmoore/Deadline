from django.test import TestCase
from .forms import UserLoginForm, RegistrationForm
from .models import User
from django.conf import settings

import logging
logger=logging.getLogger('myLogger')
# Create your tests here.
class CreateUserTests(TestCase):

    def testUserCreated(self):

        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': 'jerusalemmoore@gmail.com',
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        self.assertFalse(User.objects.filter(username=user_form_data['username']).exists())
        registration_form = RegistrationForm(data=user_form_data)
        self.assertTrue(registration_form.is_valid())
        registration_form.save()
        self.assertTrue(User.objects.filter(username=user_form_data['username']).exists())

    def testDuplicateUsernameAndEmail(self):
        duplicateEmail = settings.DEFAULT_RECIPIENT
        user = User.objects.create_user(username='jerusalemmoore', password=settings.TEST_PASSWORD, email=duplicateEmail)
        assert(user is not None)
        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': duplicateEmail,
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        registration_form = RegistrationForm(data=user_form_data)
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(
            registration_form.errors['username'][0], 'A user with that username already exists.',
        )
        self.assertEqual(
            registration_form.errors['__all__'][0], 'Account with email address ' + duplicateEmail + ' already exists'

        )
    def testValidEmail(self):
        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': 'test@',
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        registration_form = RegistrationForm(data=user_form_data)
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(
            registration_form.errors['__all__'][0], 'Enter a valid email address.'
        )

        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': 'test@.com',
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        registration_form = RegistrationForm(data=user_form_data)
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(
            registration_form.errors['__all__'][0], 'Enter a valid email address.'
        )

        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': 'test@mail.com',
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        # logger.error(registration_form.errors)
        # logger.error(registration_form.errors['__all__'])
        registration_form = RegistrationForm(data=user_form_data)
        self.assertTrue(registration_form.is_valid())
        user_form_data = {
            'username' : 'jerusalemmoore',
            'email': '@gmail.com',
            'password1' : settings.TEST_PASSWORD,
            'password2' : settings.TEST_PASSWORD
        }
        logger.error(registration_form.errors)
        registration_form = RegistrationForm(data=user_form_data)
        self.assertFalse(registration_form.is_valid())
        self.assertEqual(
            registration_form.errors['__all__'][0], 'Enter a valid email address.'
        )
# TEST YOUR PASSWORD VALIDATIONS AND MESSAGES
# test page redirection
# TEST LOGIN VALIDATION
