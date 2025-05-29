from django.shortcuts import render, get_object_or_404
from .models import Pest, Disease
from django.http import HttpResponseNotFound
from survey.models import SurveillanceRecord, Farm  # Import Farm

def home(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        survey_count = SurveillanceRecord.objects.filter(inspector=user).count()
        user_surveys = SurveillanceRecord.objects.filter(inspector=user)
        user_farms = Farm.objects.filter(owner=user)  # Get farms owned by the user
        farm_count = user_farms.count()
        context.update({
            'dashboard': True,
            'survey_count': survey_count,
            'user_surveys': user_surveys,
            'user_farms': user_farms,
            'farm_count': farm_count,
        })
    else:
        context['dashboard'] = False
    return render(request, 'home.html', context)


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
