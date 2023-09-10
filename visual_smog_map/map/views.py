"""
Views of the mapp app.

Jakub Svoboda, 2023
"""

import os
from datetime import datetime

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse

from .forms import SmogForm
from .models import Smog


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    """
    Homepage view.
    """
    return render(request, "map/index.html")


def billboards(request: HttpRequest) -> HttpResponse:
    """
    View of billboard database.
    """
    template = loader.get_template("map/billboards.html")
    smog_list = Smog.objects.all()
    context = {"smog_list": smog_list, "GOOGLE_APIKEY": str(os.getenv("GOOGLE_APIKEY"))}
    return HttpResponse(template.render(context, request))


def detail(request: HttpRequest, billboard_id: int) -> HttpResponse:
    """
    View of a single billboard with its details.
    """
    billboard = get_object_or_404(Smog, pk=billboard_id)
    return render(request, "map/detail.html", {"billboard": billboard})


def create(request: HttpRequest) -> HttpResponse:
    """
    View the form for adding new billboards.
    """
    if request.method == "POST":
        form = SmogForm(request.POST)
        if form.is_valid():
            smog_obj = form.save(commit=False)
            smog_obj.pub_date = (
                datetime.now()
            )  # Set the publication date to the current date and time
            smog_obj.save()
            return redirect("map:detail", billboard_id=smog_obj.id)
    else:
        form = SmogForm()

    return render(request, "map/create.html", {"form": form})


def save(request: HttpRequest) -> HttpResponse:
    """
    View for when a new billboard gets added.
    """
    if request.method == "POST":
        name = request.POST["name"]
        note = request.POST["note"]
        parcel = request.POST["parcel"]
        lv = request.POST["lv"]
        legality_status = request.POST["legality_status"]
        latitude = request.POST["latitude"]
        longitude = request.POST["longitude"]
        cadaster = request.POST["cadaster"]
        pub_date = request.POST["pub_date"]

        # Create the Smog object and save it to the database
        smog_obj = Smog(
            name=name,
            note=note,
            parcel=parcel,
            lv=lv,
            legality_status=legality_status,
            latitude=latitude,
            longitude=longitude,
            cadaster=cadaster,
            pub_date=pub_date,
        )
        smog_obj.save()

        return redirect(reverse("map:detail", args=[smog_obj.id]))

    return HttpResponseNotFound("POST is the only supported method.")
