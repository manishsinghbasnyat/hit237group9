from django.shortcuts import render
from models import PestInfo, DiseaseInfo
from data import pests, diseases

# Create your views here.

# from django.shortcuts import render
from .data import pest_list, disease_list

def home(request):
    return render(request, 'app_mango/home.html')

def pest_list_view(request):
    context = {
        'pests': pest_list,
        'diseases': disease_list
    }
    return render(request, 'app_mango/pest_list.html', context)


def pest_detail_view(request, item_id):
    item = next((p for p in pest_list if p.id == item_id), None)
    if item is None:
        item = next((d for d in disease_list if d.id == item_id), None)
    if item is None:
        return render(request, 'app_mango/404.html')  # Or use Django's default 404
    return render(request, 'app_mango/pest_detail.html', {'item': item})

def about(request):
    return render(request, 'app_mango/about.html')

def references(request):
    return render(request, 'app_mango/references.html')




