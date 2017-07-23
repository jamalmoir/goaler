# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth import get_user_model

from . import models


class TestUserProfileModel(TestCase):

    def test_profile_creation(self):
        User = get_user_model()
        # New user created.
        user = User.objects.create(
            username='Goaler', password='eatthatfat')
        # Check that a Profile instance has been created.
        self.assertIsInstance(user.profile, models.UserProfile)
        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instance
        user.save()
        self.assertIsInstance(user.profile, models.UserProfile)
