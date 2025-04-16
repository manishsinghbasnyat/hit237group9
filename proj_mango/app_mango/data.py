from .models import PestInfo, DiseaseInfo

# -- Adding Pests -- #
"""
pest_id,                 # Unique identifier for each pest (e.g., pest1, pest2)
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
    common_name="Mango seed weevil",
    scientific_name="Sternochetus mangiferae",
    family="Curculionidae",
    description="Eggs are creamy white, elongate and laid singly on developing fruit. Larvae are white, legless grubs with brown heads that burrow into the fruit and seed. Adults are dark brown to black, oval-shaped beetles with a long snout and mottled patterns on their backs, measuring up to 10mm in length.",
    life_cycle="One generation per year. Development from egg to adult ~53 days. Eggs laid on fruit, larvae feed inside seed.",
    damage_description="Damage is only to the seed, with sap exudate at egg laying; external symptoms not visible at harvest.",
    importance="Quarantine pest; significant in trade regulation.",
    hosts="Mangoes",
    critical_control_period="Pre-flowering and post-fruit set",
    monitoring="Inspect young fruit for egg scars and random fruit samples for larval presence in seeds.",
    comments="Remove fallen fruit to reduce populations.",
    image_url=""
)

pest2 = PestInfo(
    pest_id=2,
    common_name="Mango seed weevil",
    scientific_name="Sternochetus mangiferae",
    family="Coreidae",
    description="Eggs are oval, pale green, and laid singly on shoots or petioles. Nymphs are tear-drop shaped with a green body, red patch, and two black dots encircled in white. Adults are light to dark green with light brown backs and are agile fliers, around 15mm long.",
    life_cycle="Egg to adult: 35-42 days; 4-5 generations/year; eggs laid singly on young shoots.",
    damage_description="Lesions and cracks on shoots and young fruit; fruit drop and internal cavities in mature fruit.",
    importance="High; causes significant fruit loss.",
    hosts="Mango and other tropical fruits",
    critical_control_period="Flushing to fruit development",
    monitoring="Inspect young fruit for egg scars and random fruit samples for larval presence in seeds.",
    comments="Difficult to find; causes internal damage.",
    image_url=""
)

pest3 = PestInfo(
    pest_id=3,
    common_name="Mango fruit borer",
    scientific_name="Citripestis eutraphera",
    family="Pyralidae",
    description="Eggs are small, white, and turn reddish within 24 hours. Larvae are pinkish to red-brown with dark heads and black bands along the body. Adults are small brown moths with pale hindwings and a 20–24mm wingspan.",
    life_cycle="Egg to adult ~30 days; larvae pupate after 14 days feeding, adults live ~10 days.",
    damage_description="Frass around fruit stem; larvae tunnel into fruit, damaging flesh.",
    importance="High; affects fruit marketability.",
    hosts="Mango",
    critical_control_period="Fruit development stage",
    monitoring="Inspect fruit on tree and fallen fruit for frass and holes.",
    comments="More common in the Northern Territory.",
    image_url=""
)

pest4 = PestInfo(
    pest_id=4,
    common_name="Tea mosquito bug",  
    scientific_name="Helopeltis pernicialis",
    family="Miridae",
    description="Adults are slender reddish-brown bugs with an orange thorax and long black legs. Nymphs are golden brown and wingless. Both stages have piercing-sucking mouthparts. Eggs are inserted into plant tissue and are rarely visible.",
    life_cycle="Egg to adult: 15-30 days. Eggs laid in stems and petioles.",
    damage_description="Black necrotic lesions on shoots and fruit; corky depressions on fruit.",
    importance="Moderate to high; impacts fruit quality.",
    hosts="Mango",
    critical_control_period="Late wet season to harvest",
    monitoring="Check new flush and fruit for spotting damage.",
    comments="Prefers dense canopies; rarely seen directly.",
    image_url="image_path_or_url_here"
)

pest_list = [pest1, pest2, pest3, pest4] 


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

disease1 = DiseaseInfo(
    disease_id=1,
    common_name="Anthracnose",
    scientific_name="Colletotrichum gloeosporioides",
    type="Fungal",
    symptoms="Black spots on leaves, flower blight, fruit lesions with orange-pink spore masses, tear stains on fruit.",
    distribution="All mango growing regions in Australia; less significant in Katherine.",
    favoured_by="Rain, fog, high humidity, poor pruning and orchard hygiene.",
    similar_to="Thrips, oedema, nutritional disorders (calcium).",
    control_strategies="Pruning, orchard hygiene, fungicides (mancozeb, copper, strobilurins).",
    life_cycle="Spores germinate in moist conditions. Latent infections in fruit activate during ripening.",
    impact="Most important fungal disease of mango; can severely reduce yield and marketability.",
    image_url=""
)

disease2 = DiseaseInfo(  
    disease_id=2,
    common_name="Powdery mildew",
    scientific_name="Oidium mangiferae",
    type="Fungal",
    symptoms="White powdery growth on leaves, flowers and fruit; blackened panicles; fruit drop.",
    distribution="All regions; more common in Queensland.",
    favoured_by="Cool, dry weather interrupted by humidity.",
    similar_to="Bacterial black spot.",
    control_strategies="Broad-spectrum fungicides; varies by cultivar susceptibility.",
    life_cycle="Spores spread by wind; produced within infected tissue.",
    impact="Affects flowering and fruit set; can be significant in susceptible varieties.",
    image_url=""
)

disease3 = DiseaseInfo(
    disease_id=3,
    common_name="Mango scab",
    scientific_name="Elsinoë mangiferae",
    type="Fungal",
    symptoms="Dark brown scabs on fruit; distorted leaf margins; raised lesions on stems.",
    distribution="All regions; less significant in Katherine.",
    favoured_by="Rain and high humidity during flowering and flush.",
    similar_to="Spray or insect injury, lenticel spotting.",
    control_strategies="Preventative copper fungicides.",
    life_cycle="Spores form on lesions in wet weather; dispersed by wind and rain.",
    impact="Causes fruit blemishes and drop, reducing marketability.",
    image_url=""
)

disease_list = [disease1, disease2, disease3] 