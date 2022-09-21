from http.client import HTTPResponse
from django.shortcuts import render 
from django.http import HttpResponse
from django.core import serializers

from mywatchlist.models import MyWatchlistItem

# TODO: Create your views here.
data_mywatchlist_items = MyWatchlistItem.objects.all()
def show_mywatchlist(request):
    
    context = {
        'watchlist_items': data_mywatchlist_items,
        'nama': 'Yoozu'
    }
    return render(request, "mywatchlist.html",context)
def show_xml(request):
    
    return HttpResponse(serializers.serialize("xml", data_mywatchlist_items), content_type="application/xml")

def show_json(request):
    
    return HttpResponse(serializers.serialize("json", data_mywatchlist_items), content_type="application/json")
