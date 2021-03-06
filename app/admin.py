# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Check
from app.models import Service

class CheckAdmin(admin.ModelAdmin):
    ordering = ('-created_at','-updated_at')
    list_display = ('created_at','start_time','end_time')

class ServiceAdmin(admin.ModelAdmin):
    ordering = ('-created_at','-updated_at')
    list_display = ('created_at','hours','oil','fuel',
                    'oil_filter','fuel_filter','air_filter','refrigerant','battery')
    
admin.site.register(Check,CheckAdmin)
admin.site.register(Service,ServiceAdmin)
