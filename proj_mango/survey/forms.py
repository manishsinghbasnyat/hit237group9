from django import forms
from .models import SurveillanceRecord, Farm
import datetime
from django.utils import timezone

class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = '__all__'
        widgets = {
            'pests_found': forms.CheckboxSelectMultiple,
            'diseases_found': forms.CheckboxSelectMultiple,
            'date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'max': timezone.localdate().isoformat(),
                    'min': '2000-01-01'
                }
            ),
        }
        help_texts = {
            'date': 'Select a date between 01/01/2000 and today.',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Accept 'user' kwarg!
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields['farm'].queryset = Farm.objects.filter(owner=user)

    def clean_date(self):
        date = self.cleaned_data['date']
        min_date = datetime.date(2000, 1, 1)
        max_date = timezone.localdate()
        if date < min_date or date > max_date:
            raise forms.ValidationError(f"Date must be between {min_date.strftime('%d/%m/%Y')} and today.")
        return date
