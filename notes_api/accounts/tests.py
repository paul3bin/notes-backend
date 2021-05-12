from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('accounts:create')


def create_user(**params):
    # helper function to create a new user
    return get_user_model().objects.create_user(**params)


class ModelTests(TestCase):
    # tests for User model
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


class PublicApiTests(TestCase):
    # test the users api (public)

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user(self):
        # to test create user with valid payload is successful
        payload = {
            'email': 'testemail@gmail.com',
            'password': 'testpass',
            'name': 'Jack Reacher'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_exists(self):
        # to test creating a user that already exists
        payload = {
            'email': 'testemail@gmail.com',
            'password': 'testpass',
            'name': 'Jack Reacher'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_length(self):
        # to test that the password should be atleast 8 characters
        payload = {
            'email': 'testemail@gmail.com',
            'password': 'testpas',
            'name': 'Jack Reacher'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        # checking whether user exists or not
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
