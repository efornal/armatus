# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Check(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('created_at'))
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_('updated_at'))
    start_time = models.TimeField(
        null=False,
        verbose_name=_('start_time'))
    end_time = models.TimeField(
        null=True,
        blank=True,
        verbose_name=_('end_time'))
    operating_hours = models.TimeField(
        null=False,
        verbose_name=_('operating_hours'))
    starts = models.IntegerField(
        null=False,
        verbose_name=_('starts'))
    voltage_1 = models.IntegerField(
        null=False,
        verbose_name=_('voltage_1'))
    voltage_2 = models.IntegerField(
        null=False,
        verbose_name=_('voltage_2'))
    voltage_3 = models.IntegerField(
        null=False,
        verbose_name=_('voltage_3'))
    observation = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('description'))

    class Meta:
        db_table = 'checks'
        verbose_name = _('Check')
        verbose_name_plural = _('Checks')

    def __unicode__(self):
        return unicode(format(self.created_at, "%d-%m-%Y, %H:%S"))
