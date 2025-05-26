from django.shortcuts import render
from .data import pest_list, disease_list
from django.http import HttpResponseNotFound

# Home page view
def home(request):
    return render(request, 'app_mango/home.html')

# Pest/Disease list view
def pest_list_view(request):
    context = {
        'pests': pest_list,
        'diseases': disease_list
    }
    return render(request, 'app_mango/pest_list.html', context)

# Pest/Disease detail view with type (pest or disease)
def pest_detail_view(request, item_type, item_id):
    if item_type == 'pest':
        item = next((p for p in pest_list if p.pest_id == item_id), None)
    elif item_type == 'disease':
        item = next((d for d in disease_list if d.disease_id == item_id), None)
    else:
        return HttpResponseNotFound("Page not Found")

    if item is None:
        return HttpResponseNotFound("Page not Found")

    return render(request, 'app_mango/detail.html', {'item': item})

# About page view
def about(request):
    return render(request, 'app_mango/about.html')

# References page view
def references(request):
    return render(request, 'app_mango/references.html')
