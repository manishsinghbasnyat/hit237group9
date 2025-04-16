# app_pests/views.py
from django.shortcuts import render

# Static list of pests with prevention methods
pests_list = [
    {
        "id": 1, 
        "name": "Mango Fruit Borer", 
        "scientific_name": "Citrpestis eutraphera", 
        "description": "A pest that bores into the mango fruit, affecting its quality.", 
        "affected_parts": "Fruit",
    "image_url": "app_pests/images/Mango Fruit Borer.jpeg",
        "prevention": [
            "Monitor adult moths with pheromone traps around orchards",
            "Practice strict orchard sanitation by removing fallen fruit promptly",
            "Bag developing fruits with paper or fine mesh covers",
            "Plow orchard soil during dormant season to expose and kill pupae",
            "Maintain a clean orchard floor free of debris and weeds",
            "Harvest mature fruits as soon as possible",
            "Install light traps to catch and monitor adult moths"
        ]
    },
    {
        "id": 2, 
        "name": "Jarvis's Fruit Fly", 
        "scientific_name": "Bactrocera jarvisi", 
        "description": "A significant pest that attacks mangoes, laying eggs inside the fruit.", 
        "affected_parts": "Fruit",
    "image_url": "app_pests/images/Jarvis Fruit Fly.jpeg",
        "prevention": [
            "Monitor populations with specific pheromone traps (cue-lure)",
            "Practice thorough orchard sanitation by removing fallen and infested fruit",
            "Bag developing fruit with protective covers (paper or fine mesh)",
            "Harvest fruit at the mature green stage before they attract flies",
            "Coordinate control efforts with neighboring growers for area-wide management",
            "Till orchard soil to destroy pupating larvae",
            "Implement cold treatment protocols for harvested fruit"
        ]
    },
    {
        "id": 3, 
        "name": "Mango Leafhopper", 
        "scientific_name": "Idioscopus nitidulus", 
        "description": "Insects that feed on mango leaves, causing yellowing and wilting.", 
        "affected_parts": "Leaves",
      "image_url": "app_pests/images/Mango Leafhopper.jpeg",
        "prevention": [
            "Maintain proper tree spacing to improve air circulation",
            "Prune regularly to reduce canopy density and create less favorable habitat",
            "Time irrigation to avoid creating favorable conditions during flowering",
            "Practice intensive monitoring during flowering and new flush periods",
            "Remove weeds from orchard floor that serve as alternate hosts",
            "Avoid excessive nitrogen fertilization that promotes tender growth",
            "Install yellow sticky traps for early detection and population monitoring"
        ]
    },
    {
        "id": 4, 
        "name": "Mango Stem Miner", 
        "scientific_name": "Spulerina isonoma", 
        "description": "A pest that mines into the stem of mango trees, leading to weakened growth.", 
        "affected_parts": "Stems",
        
        "prevention": [
            "Inspect nursery stock carefully before planting or introduction",
            "Maintain good tree vigor through balanced nutrition and watering",
            "Monitor trees regularly for early signs of infestation",
            "Whitewash trunks and main branches to prevent egg laying",
            "Remove and destroy heavily infested branches during pruning",
            "Practice proper pruning technique to avoid creating entry points",
            "Implement proper spacing between trees for good air circulation"
        ]
    },
    {
        "id": 5, 
        "name": "Tea Mosquito Bug", 
        "scientific_name": "Helopeltis pernicialis", 
        "description": "A pest that damages mango fruit and leaves, causing lesions.", 
        "affected_parts": "Leaves, fruit",
        "prevention": [
            "Monitor orchards regularly during flushing and flowering",
            "Remove alternate host plants around orchards (cashew, guava, etc.)",
            "Maintain appropriate spacing between trees",
            "Prune to improve air circulation and reduce hiding places",
            "Time irrigation to avoid continuous flushing that attracts the pest",
            "Install sticky traps for early detection",
            "Avoid excess nitrogen fertilization that promotes tender growth"
        ]
    },
    {
        "id": 6, 
        "name": "Mango Seed Weevil", 
        "scientific_name": "Sternochetus mangiferae", 
        "description": "A pest that infests mango seeds, leading to reduced fruit quality.", 
        "affected_parts": "Mango seeds",
        "prevention": [
            "Implement strict quarantine measures to prevent introduction",
            "Practice thorough orchard sanitation by removing fallen fruit",
            "Destroy all infested seeds and fruits to break the life cycle",
            "Monitor adult activity with traps during emergence period",
            "Use trunk banding with sticky materials to prevent adult movement",
            "Plant resistant or less susceptible varieties when available",
            "Apply trunk wrapping to prevent adults from reaching the canopy"
        ]
    },
    {
        "id": 7, 
        "name": "Mango Planthopper", 
        "scientific_name": "Colgaroides acuminata", 
        "description": "A pest that feeds on mango sap, weakening the plant and causing stress.", 
        "affected_parts": "Sap",
        "prevention": [
            "Maintain proper tree spacing to reduce humidity and improve air flow",
            "Prune trees to allow light penetration and reduce humidity",
            "Remove weeds that serve as alternate hosts",
            "Monitor populations regularly with yellow sticky traps",
            "Avoid excessive irrigation that creates favorable conditions",
            "Control ant populations that protect planthoppers for honeydew",
            "Time pruning to avoid periods of peak planthopper activity"
        ]
    }
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