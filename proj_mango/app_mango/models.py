from django.db import models

# Create your models here.

class PestInfo:
    def __init__(
        self,
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
        image_url                # Link or path to an image of the pest
    ):
        self.pest_id = pest_id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.family = family
        self.description = description
        self.life_cycle = life_cycle
        self.damage_description = damage_description
        self.importance = importance
        self.hosts = hosts
        self.critical_control_period = critical_control_period
        self.monitoring = monitoring
        self.comments = comments
        self.image_url = image_url


        

class DiseaseInfo:
    def __init__(
        self,
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
    ):
        self.disease_id = disease_id
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.type = type
        self.symptoms = symptoms
        self.distribution = distribution
        self.favoured_by = favoured_by
        self.similar_to = similar_to
        self.control_strategies = control_strategies
        self.life_cycle = life_cycle
        self.impact = impact
        self.image_url = image_url
