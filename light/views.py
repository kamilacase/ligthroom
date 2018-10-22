# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView
# Create your views here.
from .models import Light, LIGHT_STATUS_CHOICES

from .froms import LightFom

from django.core.urlresolvers import reverse_lazy

from django.http import JsonResponse


class LightListView(ListView):
    model = Light
    def get_context_data(self, **kwargs):
        context = ListView.get_context_data(self, **kwargs)

        context['lights'] = []
        for light in self.get_queryset():
            context['lights'].append({
                'light': light,
                'from': LightFom(instance=light)
            })

        return context


class LightSwitchView(UpdateView):
    model = Light
    form_class = LightFom
    success_url = reverse_lazy('light_list')

    def form_valid(self, form):
        return JsonResponse({
        'id': self.object.id,
        'status': self.object.status,
        })
