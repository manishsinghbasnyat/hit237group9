from django.db import models

class Pest(models.Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    family = models.CharField(max_length=50)
    description = models.TextField()
    life_cycle = models.TextField()
    damage_description = models.TextField()
    importance = models.TextField()
    hosts = models.CharField(max_length=200)
    critical_control_period = models.CharField(max_length=100)
    monitoring = models.TextField()
    comments = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=True)  # or use FileField/URLField

    def __str__(self):
        return self.common_name

class Disease(models.Model):
    DISEASE_TYPES = [
        ('Fungal', 'Fungal'),
        ('Bacterial', 'Bacterial'),
        ('Viral', 'Viral'),
        # Add more as needed
    ]
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=DISEASE_TYPES)
    symptoms = models.TextField()
    distribution = models.CharField(max_length=200)
    favoured_by = models.CharField(max_length=200)
    similar_to = models.CharField(max_length=200)
    control_strategies = models.TextField()
    life_cycle = models.TextField()
    impact = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=True)  # or use FileField/URLField

    def __str__(self):
        return self.common_name
