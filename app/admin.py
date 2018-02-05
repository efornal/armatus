# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from app.models import Check

# Register your models here.
    
class CheckAdmin(admin.ModelAdmin):
    ordering = ('created_at','updated_at')
    
admin.site.register(Check,CheckAdmin)
