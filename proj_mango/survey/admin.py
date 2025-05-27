from django.contrib import admin
from .models import Farm, SurveillanceRecord

# Register your models here.
admin.site.register(Farm)
admin.site.register(SurveillanceRecord)
