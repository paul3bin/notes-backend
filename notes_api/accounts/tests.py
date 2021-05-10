from django.test import TestCase
from django.contrib.auth import get_user_model

# tests for User model


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        # to test creating a new user with email
        email = 'testemail@gmail.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # to test whether the email for a new user is normalized or not.
        email = 'testemail@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'testpassword')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # to test creating a new user with no email
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testpassword')

    def test_create_new_superuser(self):
        # to test creating a new super user
        user = get_user_model().objects.create_superuser(
            'testemail@gmail.com',
            'testpassword'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
