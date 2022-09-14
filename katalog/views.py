from django.shortcuts import render 

from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_catalog_items = CatalogItem.objects.all()
    context = {
        'catalog_items': data_catalog_items,
        'nama': 'Yoozu'
    }
    return render(request, "katalog.html",context)
