"""
URL routing mapping for the map app.

Jakub Svoboda, 2023
"""

from typing import List

from django.urls import URLPattern, path

from . import views

app_name = "map"
urlpatterns: List[URLPattern] = [
    path("", views.index, name="index"),
    # ex: /billboards/
    path("billboards/", views.billboards, name="billboards"),
    # ex: /billboards/5/
    path("billboards/<int:billboard_id>/", views.detail, name="detail"),
    # ex: /billboards/create
    path("billboards/create/", views.create, name="create"),
    # ex: /billboards/save
    path("billboards/save/", views.save, name="save"),
]
