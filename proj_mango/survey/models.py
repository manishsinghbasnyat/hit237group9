from django.db import models
from catalog.models import Pest, Disease  # Import from Catalog App
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

User = get_user_model()

class Farm(models.Model):
    """
    Represents a farm or property where surveillance is conducted.
    Each farm is owned by a user (owner).
    """
    name = models.CharField(
        max_length=100,
        blank=False,
        help_text="Enter the farm's name."
    )
    farm_address = models.CharField(
        max_length=255,
        blank=True,
        help_text="Enter the farm's address."
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='farms',
        help_text="Farm owner (user account)."
    )
    contact_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+?[\d\s\-]{7,20}$',
                message="Enter a valid phone number (digits, spaces, dashes, and optional leading +)."
            )
        ],
        help_text="Enter a valid contact number."
    )
    notes = models.TextField(
        blank=True,
        help_text="Additional notes (optional)."
    )
    # --- New compulsory fields ---
    land_area = models.DecimalField(
        max_digits=10,  # Total number of digits
        decimal_places=2,  # Number of digits after the decimal point
        blank=False,
        default=0.0,
        help_text="Land area (acres or hectares)."
    )
    num_trees_est = models.PositiveIntegerField(
        verbose_name="Number of Trees (Estimated)",
        default=0,
        blank=False,
        help_text="Estimated number of trees."
    )

    def __str__(self):
        return self.name

class SurveillanceRecord(models.Model):
    """
    Represents a surveillance or inspection event.
    """
    farm = models.ForeignKey(
        Farm,
        on_delete=models.CASCADE,
        related_name='surveillance_records'
    )
    date = models.DateField(
        help_text="Select a date between 01/01/2000 and today."
    )
    inspector = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="The user who conducted the surveillance."
    )
    
    num_trees_inspected = models.PositiveIntegerField(
        verbose_name="Number of Trees Inspected",
        default=0,
        help_text="Enter the number of trees inspected during this survey."
    )
    
    pests_found = models.ManyToManyField(
        Pest,
        blank=True,
        help_text="Select all pests found (if any)."
    )
    diseases_found = models.ManyToManyField(
        Disease,
        blank=True,
        help_text="Select all diseases found (if any)."
    )
    notes = models.TextField(
        blank=False,
        max_length=1000,
        help_text="Notes taken during survey. Type 'N/A' if none."
    )
    image = models.ImageField(
        upload_to='survey/',
        blank=True,
        null=True,
        help_text="Upload an image (optional)."
    )


    def __str__(self):
        return f"Survey at {self.farm.name} on {self.date}"

