from django.db import models

# Create your models here.
class PestInfo:
    def __init__(self, id, name, short_description, long_description, image_url):
        self.id = id
        self.name = name
        self.short_description = short_description
        self.long_description = long_description
        self.image_url = image_url