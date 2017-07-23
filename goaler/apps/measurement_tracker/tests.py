# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth import get_user_model


class TestMeasurementModel(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(
            username='Goaler', password='eatthatfat')
        self.profile = self.user.profile

    def tearDown(self):
        self.user.delete()
