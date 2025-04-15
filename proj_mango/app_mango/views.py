from django.shortcuts import render
from data import items

# Create your views here.

def pest_list(request):
    # passes the list of pests & diseases to the template
    return render(request, 'pests/pest_list.html', {'items': items})