# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from rents.models import Rent, RentType
from users.tests.factories import UserFactory


class RentTestCase(TestCase):

    def setUp(self):
        self.rent_types = RentType.objects.all()
        self.user = UserFactory()

    def test_simple_rent(self):
        rent_type = self.rent_types[0]
        rent = Rent.objects.create(
            rent_type=rent_type,
            user=self.user,
        )

        self.assertEqual(rent.price, rent_type.price)

    def test_familiar_rent(self):
        rent_type = self.rent_types[0]
        rent = Rent.objects.create(
            rent_type=rent_type,
            user=self.user,
            quantity=4
        )

        self.assertEqual(rent.price, rent_type.price * 4 * .7)

    def test_error_rent(self):
        rent_type = self.rent_types[0]
        rent = Rent.objects.create(
            rent_type=rent_type,
            user=self.user,
            quantity=6
        )

        self.assertFalse(rent.price, rent_type.price * 6 * .7)
