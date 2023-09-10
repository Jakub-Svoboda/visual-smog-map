"""
Contains input forms specification.

Jakub Svoboda, 2023
"""

from django import forms

from .models import Smog


class SmogForm(forms.ModelForm):
    """
    Basic input form for adding new billboards to the system.
    """

    class Meta:
        model = Smog
        fields = [
            "name",
            "note",
            "parcel",
            "lv",
            "legality_status",
            "latitude",
            "longitude",
            "cadaster",
        ]

    LEGALITY_STATUS_CHOICES = [
        ("Legal", "Legal"),
        ("Illegal", "Illegal"),
        ("Unknown", "Unknown"),
    ]

    legality_status = forms.ChoiceField(choices=LEGALITY_STATUS_CHOICES)
    latitude = forms.DecimalField(max_digits=9, decimal_places=6)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6)
