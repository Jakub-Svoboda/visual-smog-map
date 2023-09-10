"""
App registration.

Jakub Svoboda, 2023
"""

from django.apps import AppConfig


class MapConfig(AppConfig):
    """
    Configuration for the Map App.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "map"
