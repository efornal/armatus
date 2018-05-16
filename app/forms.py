# -*- coding: utf-8 -*-
from django import forms
import logging
from .models import Check
from datetimewidget.widgets import DateTimeWidget
from django.utils.translation import ugettext as _
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from durationfield.forms import DurationField as FDurationField
from django.conf import settings


class CheckForm(forms.ModelForm):
    start_time = forms.TimeField(
        required=False,
        label=_('start_time'))
    end_time = forms.TimeField(
        required=False,
        label=_('end_time'))
    operating_hours = FDurationField(
        required=True,
        label=_('operating_hours'))
    starts = forms.IntegerField(
        required=True,
        label=_('starts'))
    voltage_1 = forms.IntegerField(
        required=True,
        label=_('voltage_1'))
    voltage_2 = forms.IntegerField(
        required=True,
        label=_('voltage_2'))
    voltage_3 = forms.IntegerField(
        required=True,
        label=_('voltage_3'))
    tank = forms.DecimalField(
        required=True,
        max_value=1,
        min_value=0,
        max_digits=3,
        decimal_places=3,
        label=_('tank'))
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name = "id",
        required = True,
        label=_('user'))
    observations = forms.CharField(
        required=False,
        widget=forms.Textarea,
        label=_('observations'))

    def clean(self):
        cleaned_data = super(CheckForm, self).clean()

    class Meta:
        model = Check
        fields = ('start_time', 'end_time', 'operating_hours','starts','tank',
                  'voltage_1','voltage_2','voltage_3','user','observations')
