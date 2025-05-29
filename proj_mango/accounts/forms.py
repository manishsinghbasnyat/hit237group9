from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from survey.models import Farm  # Import the Farm model

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, label='First name')
    last_name = forms.CharField(max_length=30, required=True, label='Last name')
    email = forms.EmailField(max_length=254, required=True, label='Email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# Form for Add_Farm
class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = '__all__'  # This will include all fields from farm