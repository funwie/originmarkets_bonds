from decimal import  *

from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse


# initialize the APIClient to use for testing
from applications.bond.models import Bond
from applications.bond.serializers import BondSerializer

client = Client()

bond = {
    "isin": "FR0000131104",
    "size": 100000000,
    "currency": "EUR",
    "maturity": "2025-02-28",
    "lei": "R0MUWSFPU8MPRO8K5P83"
}


class GetBondDetailTest(TestCase):
    """ Test module for GET bond api/bonds/1"""

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="bar12345")
        client.login(username='testuser', password='bar12345')
        bond['owner'] = self.user
        self.bond = Bond.objects.create(**bond)

    def test_get_valid_single_bond(self):
        response = client.get(reverse('bond-detail', kwargs={'pk': self.bond.pk}))
        order = Bond.objects.get(pk=self.bond.pk)
        serializer = BondSerializer(order)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_bond(self):
        response = client.get(
            reverse('bond-detail', kwargs={'pk': 10}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
