# -*- encoding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from . import managers


class Measurement(models.Model):
    # Relations
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='measurements',
        verbose_name=_('user'),
    )

    # Attributes - Mandatory
    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        verbose_name=_('weight'),
        help_text=_('Enter your body weight'),
    )

    date = models.DateField(
        verbose_name=_('date'),
        default=timezone.now,
    )

    # Attributes - Optional
    neck = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('neck'),
        help_text=('Enter your neck circumference'),
    )

    chest = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('chest'),
        help_text=('Enter your chest circumference'),
    )

    arm = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('arm'),
        help_text=('Enter your arm circumference'),
    )

    waist = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('waist'),
        help_text=('Enter your waist circumference'),
    )

    hip = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('hip'),
        help_text=('Enter your hip circumference'),
    )

    thigh = models.FloatField(
        null=True,
        validators=[MinValueValidator(0.0)],
        verbose_name=('thigh'),
        help_text=('Enter your thigh circumference'),
    )

    # Object Manager
    objects = managers.MeasurementManager()

    # Custom Properties

    # Methods

    # Meta and String
    class Meta:
        verbose_name = _('Measurement')
        verbose_name_plural = _('Measurements')
        ordering = ('user', 'date')
        # unique_together = ('user', 'date')

    def __str__(self):
        return '{}kg'.format(self.weight)
