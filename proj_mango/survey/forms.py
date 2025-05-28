from django import forms
from .models import SurveillanceRecord

class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = ['farm', 'date', 'pests_found', 'diseases_found', 'notes', 'image']
        widgets = {
            'pests_found': forms.CheckboxSelectMultiple,
            'diseases_found': forms.CheckboxSelectMultiple,
        }
