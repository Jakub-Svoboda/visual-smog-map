"""
Admin settings and model registration.

Jakub Svoboda, 2023
"""

from django.contrib import admin

from .models import Smog

# Register your models here.
admin.site.register(Smog)
