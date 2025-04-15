# app_pests/pests_data.py

class PestDisease:
    def __init__(self, name, description, image_url):
        self.name = name
        self.description = description
        self.image_url = image_url

# Creating instances for 7 mango pests/diseases
pests_list = [
    PestDisease(
        'Mango Anthracnose', 
        'A fungal disease affecting mango trees that causes dark lesions on fruit and leaves.', 
        '/static/images/MangoAnthracnose.jpg'
    ),
    PestDisease(
        'Mango Mealybug', 
        'An insect pest that sucks sap from mango trees, weakening the plant and causing deformed fruit.', 
        '/static/images/mealybug.jpg'
    ),
    PestDisease(
        'Mango Fruit Fly', 
        'A major pest that attacks mangoes and other fruits, laying eggs inside the fruit.', 
        '/static/images/fruit_fly.jpg'
    ),
    PestDisease(
        'Mango Hoppers', 
        'Insects that attack mango trees and leave sticky sap, attracting ants and fungi.', 
        '/app_pests/static/images/Mango Hoppers.jpg'
    ),
    PestDisease(
        'Bacterial Black Spot', 
        'A bacterial disease that causes dark, necrotic spots on mango leaves and fruit.', 
        '/static/images/black_spot.jpg'
    ),
    PestDisease(
        'Mango Leaf Spot', 
        'A fungal infection that causes circular spots on mango leaves, reducing the tree’s ability to photosynthesize.', 
        '/static/images/leaf_spot.jpg'
    ),
    PestDisease(
        'Mango Stem Borer', 
        'A pest that bores into the trunk of mango trees, weakening the plant and causing dieback.', 
        '/static/images/mango_fruit_borer.jpg'
    )
]
