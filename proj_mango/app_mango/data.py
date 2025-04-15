from models import PestInfo, DiseaseInfo

# -- Adding Pests -- #

pests = [
    PestInfo(
        id=1,
        name="Fruit Fly",
        short_description="A major pest affecting mangoes.",
        long_description="Fruit flies lay eggs inside the fruit, causing rotting and reducing yield.",
        image_url="fruitfly.jpg"
    ),

  PestInfo(
        id=2,
        name="name2",
        short_description="A major pest affecting mangoes.",
        long_description="Fruit flies lay eggs inside the fruit, causing rotting and reducing yield.",
        image_url="fruitfly.jpg"
    ),

]





# -- Adding Diseases -- #

diseases = [
    
DiseaseInfo(
        id=1,
        name="Powdery Mildew",
        short_description="A fungal disease affecting mango trees.",
        long_description="Powdery mildew causes white, powdery spots on leaves and fruit, reducing plant health.",
        image_url="powdery_mildew.jpg"
),

DiseaseInfo(
        id=2,
        name="Disease2",
        short_description="Disease 2 desc",
        long_description="Powdery mildew causes white, powdery spots on leaves and fruit, reducing plant health.",
        image_url="powdery_mildew.jpg"
),

]