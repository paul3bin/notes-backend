from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

GET_NOTES_LIST = reverse("notes:get")
CREATE_NOTE = reverse("notes:create")


def note_update_url(note_id):
    # returns note update url
    return reverse("notes:update", args=[note_id])


def note_delete_url(note_id):
    # returns note delete url
    return reverse("notes:delete", args=[note_id])


class PublicNotesApiTests(TestCase):
    # to test unauthenicated notes api access

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        # to test that authentication is required
        res = self.client.get(GET_NOTES_LIST)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
