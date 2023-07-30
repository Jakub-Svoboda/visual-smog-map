from django.urls import path

from . import views

app_name = 'map'
urlpatterns = [
    path('', views.index, name='index'),
    # ex: /map/
    path('map/', views.map, name='map'),
    # ex: /billboards/
    path('billboards/', views.billboards, name='billboards'),
    # ex: /billboards/5/
    path('billboards/<int:billboard_id>/', views.detail, name='detail'),
    # ex: /billboards/create
    path('billboards/create/', views.create, name='create'),
    # ex: /billboards/save
    path('billboards/save/', views.save, name='save')
]