from django.shortcuts import render
from .models import PestInfo, DiseaseInfo
from .data import pest_list, disease_list
from django.http import HttpResponseNotFound

# Create your views here.

# Home Page View
# Renders the home page with a basic introduction and overview.
def home(request):
    context = {
        'pests': pest_list,  # A list of all pests
        'diseases': disease_list  # A list of all diseases
    }
    return render(request, 'app_mango/home.html')

# Pest & Disease List View
# Renders the page that lists all pests and diseases.
# Passes the full pest_list and disease_list to the template.
def pest_disease_list(request):
    context = {
        'pests': pest_list,  # List of all pests to be displayed
        'diseases': disease_list  # List of all diseases to be displayed
    }
    return render(request, 'app_mango/pest_disease_list.html', context)


# Pest Detail View
# Renders a page showing details for a specific pest.
# Looks up the pest by its ID from the pest_list.
# If the pest is not found, returns a 404 error page.
def pest_detail(request, pest_id):
    # Searching for the pest with the given ID in the pest_list
    pest = next((p for p in pest_list if p.pest_id == pest_id), None)
    
    # If pest is not found, return a 404 error response
    if pest is None:
        return HttpResponseNotFound("Pest not found.")
    
    # If pest is found, render the pest_detail page with the pest data
    return render(request, 'app_mango/pest_detail.html', {'pest': pest})

# Disease Detail View
# Renders a page showing details for a specific disease.
# Looks up the disease by its ID from the disease_list.
# If the disease is not found, returns a 404 error page.
def disease_detail(request, disease_id):
    # Searching for the disease with the given ID in the disease_list
    disease = next((d for d in disease_list if d.disease_id == disease_id), None)
    
    # If disease is not found, return a 404 error response
    if disease is None:
        return HttpResponseNotFound("Disease not found.")
    
    # If disease is found, render the disease_detail page with the disease data
    return render(request, 'app_mango/disease_detail.html', {'disease': disease})

# About Page View
# Renders the about page with team member names and student IDs.
def about(request):
    return render(request, 'app_mango/about.html')