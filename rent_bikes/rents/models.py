# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class RentType(TimeStampedModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()  # Price in cents


class Rent(TimeStampedModel):
    rent_type = models.ForeignKey('RentType')
    quantity = models.PositiveSmallIntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    price = models.PositiveIntegerField()  # Price in cents

    def clean(self):
        if self.quantity > 5:
            raise ValidationError(_('You can\'t rent more than 5 bikes.'))

    def save(self, *args, **kwargs):
        if self.quantity > 5:
            return

        self.price = self.rent_type.price * self.quantity

        # apply discount for 3 or more
        if self.quantity >= 3:
            self.price *= .7

        super(Rent, self).save(*args, **kwargs)
