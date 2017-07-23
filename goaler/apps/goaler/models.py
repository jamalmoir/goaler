# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver

from . import managers


class UserProfile(models.Model):
    # Relations
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name='profile',
        verbose_name=_('user'),
    )

    # Attributes - Mandatory
    interaction = models.PositiveIntegerField(
        default=0,
        verbose_name=_('interaction'),
    )

    # Attributes - Optional
    date_of_birth = models.DateField(
        null=True,
        verbose_name=_('date of birth'),
    )

    sex = models.CharField(
        null=True,
        max_length=1,
        choices=(('M', 'Male'), ('F', 'Female')),
        verbose_name=_('sex'),
    )

    # Object Manager
    objects = managers.UserProfileManager()

    # Custom Properties
    @property
    def username(self):
        return self.user.username

    # Methods

    # Meta and String
    class Meta:
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')
        ordering = ('user',)

        def __str__(self):
            return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()
