from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Smog

# Create your views here.
def index(request):
    return render(request, 'map/index.html')

def map(request):
    return HttpResponse('You\'re looking at a map billboards.')

def billboards(request):
    template = loader.get_template('map/billboards.html')
    smog_list = Smog.objects.all()
    context = {
        'smog_list': smog_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, billboard_id):
    billboard = get_object_or_404(Smog, pk=billboard_id)
    return render(request, 'map/detail.html', {'billboard': billboard})

def create(request):
     #return HttpResponse('You\'re creating new billboard record.')
    return render(request, 'map/create.html')

def save(request):
    if request.method == 'POST':
        name = request.POST['name']
        note = request.POST['note']
        parcel = request.POST['parcel']
        lv = request.POST['lv']
        legality_status = request.POST['legality_status']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        cadaster = request.POST['cadaster']
        pub_date = request.POST['pub_date']

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

        return redirect(reverse('map:detail', args=[smog_obj.id]))

