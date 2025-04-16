from django.shortcuts import render
from .data import pest_list, disease_list
from django.http import HttpResponseNotFound

# Create your views here.

# from django.shortcuts import render
from .data import pest_list, disease_list

def home(request):
    return render(request, 'app_mango/home.html') # For home page

def pest_list_view(request):
    context = {
        'pests': pest_list,
        'diseases': disease_list
    }
    return render(request, 'app_mango/pest_list.html', context) # for pest/disease list


def pest_detail_view(request, item_id):
    item = next((p for p in pest_list if p.pest_id == item_id), None)
    if item is None:
        item = next((d for d in disease_list if d.disease_id == item_id), None)
    if item is None:
        return HttpResponseNotFound("Page not Found")
    return render(request, 'app_mango/detail.html', {'item': item})

def about(request):
    return render(request, 'app_mango/about.html')

def references(request):
    return render(request, 'app_mango/references.html')




