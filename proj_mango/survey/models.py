from django.db import models
from catalog.models import Pest, Disease  # Import from catalog app
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Property(models.Model):
    """
    Represents a property or farm where surveillance is conducted.
    """
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    owner = models.CharField(max_length=100, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SurveillanceRecord(models.Model):
    """
    Represents a surveillance or inspection event.
    """
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='surveillance_records')
    date = models.DateField()
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pests_found = models.ManyToManyField(Pest, blank=True)
    diseases_found = models.ManyToManyField(Disease, blank=True)
    notes = models.TextField(blank=True)
    image = models.ImageField(upload_to='survey/', blank=True, null=True)

    def __str__(self):
        return f"Survey at {self.property.name} on {self.date}"

