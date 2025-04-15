from .models import PestInfo, DiseaseInfo

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
    common_name="Aphid",
    scientific_name="Aphis spp.",
    family="Aphididae",
    description="Aphids are small sap-sucking insects that damage plants in the nymph and adult stages.",
    life_cycle="Egg > Nymph > Adult. Life cycle is completed in 7-14 days.",
    damage_description="Aphids cause deformed growth, yellowing of leaves, and can transmit plant viruses.",
    importance="Aphids are a significant pest for many crops, including vegetables and fruits.",
    hosts="Cabbage, Lettuce, Roses, Peas, and many other plants.",
    critical_control_period="Spring and early summer when populations explode.",
    monitoring="Regular inspection of leaves, especially on the underside for colonies.",
    comments="Aphids are known for their rapid reproduction and ability to cause major crop loss if not controlled.",
    image_url="images/aphid.jpg"
)

pest2 = PestInfo(
    pest_id=2,
    common_name="Whitefly",
    scientific_name="Bemisia tabaci",
    family="Aleyrodidae",
    description="Whiteflies are tiny, winged insects that suck sap from the undersides of leaves.",
    life_cycle="Egg > Nymph > Adult. Can complete a cycle in 2-3 weeks.",
    damage_description="Whiteflies cause yellowing, leaf drop, and black sooty mold from excreted honeydew.",
    importance="Whiteflies are known for causing severe damage to crops and transmitting plant diseases.",
    hosts="Tomato, Cucumber, Cotton, Eggplant.",
    critical_control_period="During the growing season when environmental conditions favor rapid breeding.",
    monitoring="Use yellow sticky traps to monitor adult whitefly populations.",
    comments="Whiteflies are resistant to many pesticides, so integrated pest management is critical.",
    image_url="images/whitefly.jpg"
)

pest_list = [pest1, pest2]


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

# -- Adding Diseases -- #

disease1 = DiseaseInfo(
    disease_id=1,
    common_name="Anthracnose",
    scientific_name="Colletotrichum gloeosporioides",
    type="Fungal",
    symptoms="Large brown lesions on leaves, fruits, and stems. Tip dieback of branches.",
    distribution="Tropical and subtropical regions, including parts of Australia.",
    favoured_by="High humidity and wet conditions. The disease thrives during the rainy season.",
    similar_to="Calcium deficiency, but can be differentiated by the appearance of dark lesions.",
    control_strategies="Fungicides, pruning infected plant parts, and improving air circulation around plants.",
    life_cycle="Spore germination and infection occur during wet conditions, spreading through rain or irrigation.",
    impact="Severe yield losses in susceptible crops like mango, avocados, and citrus.",
    image_url="images/anthracnose.jpg"
)

disease2 = DiseaseInfo(
    disease_id=2,
    common_name="Powdery Mildew",
    scientific_name="Erysiphe spp.",
    type="Fungal",
    symptoms="White powdery spots on leaves and stems. Deformed or stunted plant growth.",
    distribution="Common in temperate regions. Found globally on a wide range of plants.",
    favoured_by="Dry weather, with high humidity in the morning and cooler evenings.",
    similar_to="Could be confused with downy mildew, but powdery mildew has a distinct powdery appearance.",
    control_strategies="Use fungicides, remove infected plant parts, and space plants to increase airflow.",
    life_cycle="Spores are airborne and can infect plants under dry conditions.",
    impact="Can weaken plants, reducing photosynthesis and yield, especially in fruit crops like cucumbers and melons.",
    image_url="images/powdery_mildew.jpg"
)

disease_list = [disease1, disease2]