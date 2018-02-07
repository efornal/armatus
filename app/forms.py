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

CHOICES = (
    ('0', _('empty')),
    ('0.125', '1/8',),
    ('0.25', '1/4',),
    ('0.375', '3/8',),
    ('0.5', '1/2',),
    ('0.625', '5/8',),
    ('0.375', '3/4',),
    ('0.875', '7/8',),
    ('1', _('full')))

def clean_tank_value(value):
    return value.replace('[','') \
                .replace(']','') \
                .replace('u','') \
                .replace("'","") 

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
    tank = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES,
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name = "id",
        required = True,
        label=_('user'))

    def clean(self):
        cleaned_data = super(CheckForm, self).clean()

    def clean_tank(self):
        value = self.cleaned_data.get('tank')
        value = clean_tank_value(value[0])
        return value

    class Meta:
        model = Check
        fields = ('start_time', 'end_time', 'operating_hours','starts','tank',
                  'voltage_1','voltage_2','voltage_3','user')
