from django.shortcuts import render
from .models import PestInfo, DiseaseInfo
from .data import pest_list, disease_list
from django.http import HttpResponseNotFound

# Create your views here.

# Home Page View
def home(request):
    return render(request, 'app_mango/home.html')


# Pest & Disease Combined List View
def pest_disease_list(request):
    return render(request, 'app_mango/pest_disease_list.html', {
        'pest_list': pest_list,
        'disease_list': disease_list
    })


def pest_detail(request, pest_id):
    pest = next((p for p in pest_list if p.pest_id == pest_id), None)
    if pest is None:
        return HttpResponseNotFound("Pest not found.")
    return render(request, 'app_mango/pest_detail.html', {'pest': pest})

def disease_detail(request, disease_id):
    disease = next((d for d in disease_list if d.disease_id == disease_id), None)
    if disease is None:
        return HttpResponseNotFound("Disease not found.")
    return render(request, 'app_mango/disease_detail.html', {'disease': disease})


# About Page View
def about(request):
    return render(request, 'app_mango/about.html')


