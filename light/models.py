# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

LIGHT_STATUS_CHOICES = (
    ('ON', 'allumé'),
    ('OFF', 'Eteint'),
)

class Light(models.Model):
    status = models.CharField(max_length=5, null=False, choices=LIGHT_STATUS_CHOICES, default='OFF')

    def __unicode__(self):
        return "LIGHT #%s [%s]" %(self.id, self.status)
