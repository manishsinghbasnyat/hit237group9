# app_pests/views.py
from django.shortcuts import render

# Static list of pests
pests_list = [
    {"id": 1, "name": "Mango Hopper", "description": "A pest that affects mango trees, causing leaf curling and stunted growth.", "affected_parts": "Leaves, stems"},
    {"id": 2, "name": "Mango Seed Weevil", "description": "A weevil that bores into mango seeds and can destroy them.", "affected_parts": "Mango seeds"},
    {"id": 3, "name": "Fruit Fly", "description": "Fruit flies cause ripened mangoes to spoil.", "affected_parts": "Fruit"},
    {"id": 4, "name": "Red Gum Lerp Psyllid", "description": "A sap-sucking insect that can cause mango trees to weaken and produce poor fruit.", "affected_parts": "Leaves, stems"},
    {"id": 5, "name": "Mango Fruit Borer", "description": "A pest that bores into the mango fruit, affecting its quality.", "affected_parts": "Fruit"},
    {"id": 6, "name": "Mealybug", "description": "A pest that feeds on the mango tree and causes damage to the fruit and leaves.", "affected_parts": "Leaves, fruit"},
    {"id": 7, "name": "Mango Bark Borer", "description": "A pest that affects the bark of the mango tree and weakens the tree.", "affected_parts": "Bark"}
]

def home_view(request):
    return render(request, 'app_pests/home.html')

def pests_list_view(request):
    return render(request, 'app_pests/pests_list.html', {'pests': pests_list})

def pest_detail_view(request, id):
    # Find pest by ID from the static list
    pest = next((p for p in pests_list if p['id'] == id), None)
    return render(request, 'app_pests/pest_detail.html', {'pest': pest})
def about_view(request):
    return render(request, 'app_pests/about.html')