# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.
from .models import Light, LIGHT_STATUS_CHOICES

class LightListView(ListView):
    model = Light
