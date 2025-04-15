from models import PestInfo, DiseaseInfo

# -- Adding Pests -- #
"""
pest_id,                  # Unique identifier for each pest (e.g., pest1, pest2)
common_name,             # Common name of the pest
scientific_name,         # Scientific name of the pest
family,                  # Family classification of the pest
description,             # Description of pest stages (egg, immature, adult)
life_cycle,              # Pest's developmental stages and duration
damage_description,      # Nature of damage caused by the pest
importance,              # Significance or severity of the pest
hosts,                   # Host plants or crops affected
critical_control_period, # Period when pest control is most crucial
monitoring,              # Monitoring methods and indicators
comments,                # Additional notes or observations
image_url                # Link or path to an image of the pest"""

pest1 = PestInfo(
    pest_id=1,
    common_name="Hello Hello",
    scientific_name="",
    family="",
    description="",
    life_cycle="",
    damage_description="",
    importance="",
    hosts="",
    critical_control_period="",
    monitoring="",
    comments="",
    image_url=""
)





pest_list = [pest1,]


# -- Adding Diseases -- #

# Structure
"""
disease_id,          # Unique identifier for each disease (e.g., disease1, disease2)
common_name,         # Common name (e.g., Anthracnose)
scientific_name,     # Scientific name (e.g., Colletotrichum gloeosporioides)
type,                # Type of disease (e.g., Fungal, Bacterial, Viral)
symptoms,            # Key symptoms (e.g., Large brown lesions, tip dieback, etc.)
distribution,        # Geographic spread or regions affected (e.g., Darwin region)
favoured_by,         # Environmental/host conditions that promote it (e.g., high humidity)
similar_to,          # Other conditions it may resemble (e.g., calcium deficiency)
control_strategies,  # Management/prevention methods (e.g., fungicide, pruning)
life_cycle,          # How it spreads and survives (e.g., spore germination)
impact,              # Effects on plant health/yield (optional)
image_url            # URL or path to an image of the disease

"""

disease1=DiseaseInfo(
    disease_id=1,
    common_name="",
    scientific_name="",
    
    
    )