from django.shortcuts import render, get_object_or_404
from .models import Pest, Disease
from django.http import HttpResponseNotFound

# Home page view
def home(request):
    return render(request, 'catalog/home.html')

# Pest/Disease list view
def pest_list_view(request):
    pests = Pest.objects.all()
    diseases = Disease.objects.all()
    context = {
        'pests': pests,
        'diseases': diseases
    }
    return render(request, 'catalog/pest_list.html', context)

# Pest/Disease detail view with type (pest or disease)
def pest_detail_view(request, item_type, item_id):
    if item_type == 'pest':
        item = get_object_or_404(Pest, pk=item_id)
    elif item_type == 'disease':
        item = get_object_or_404(Disease, pk=item_id)
    else:
        return HttpResponseNotFound("Page not Found")

    # Pass item_type to the template for template logic
    return render(request, 'catalog/detail.html', {'item': item, 'item_type': item_type})

# About page view
def about(request):
    return render(request, 'catalog/about.html')

# References page view
def references(request):
    return render(request, 'catalog/references.html')
