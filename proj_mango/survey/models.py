from django.db import models
from catalog.models import Pest, Disease # Import from Catalog App
from django.contrib.auth import get_user_model

User = get_user_model()

class Farm(models.Model):
    """
    Represents a farm or property where surveillance is conducted.
    """
    name = models.CharField(max_length=100)
    farm_address = models.CharField(max_length=255, blank=True)  # Renamed from 'address'
    owner = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SurveillanceRecord(models.Model):
    """
    Represents a surveillance or inspection event.
    """
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='surveillance_records')
    date = models.DateField()
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pests_found = models.ManyToManyField(Pest, blank=True)
    diseases_found = models.ManyToManyField(Disease, blank=True)
    notes = models.TextField(blank=True, max_length=1000)
    image = models.ImageField(upload_to='survey/', blank=True, null=True)

    def __str__(self):
        return f"Survey at {self.farm.name} on {self.date}"
