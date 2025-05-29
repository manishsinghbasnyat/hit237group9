from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
from survey.models import Farm
from django import forms

# Registration view for new users
def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect('home') 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_view')
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register_user.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')

# Add Farm
@login_required
def add_farm_view(request):
    class FarmForm(forms.ModelForm):
        class Meta:
            model = Farm
            fields = '__all__'

    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Farm added successfully!")
            return redirect('/survey/')
    else:
        form = FarmForm()
    return render(request, 'accounts/add_update_farm.html', {'form': form, 'farm': None})

# Farm Detail View - anyone logged in can view
@login_required
def farm_detail_view(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    return render(request, 'accounts/farm_detail.html', {'farm': farm})

# Update Farm Details - only owner can update
@login_required
def farm_update_view(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if farm.owner != request.user:
        messages.error(request, "You do not have permission to edit this farm.")
        return redirect('farm_detail', pk=farm.pk)
    class FarmForm(forms.ModelForm):
        class Meta:
            model = Farm
            fields = ['name', 'farm_address', 'contact_number', 'notes']  # Owner not editable
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            messages.success(request, "Farm updated successfully!")
            return redirect('farm_detail', pk=farm.pk)
    else:
        form = FarmForm(instance=farm)
    return render(request, 'accounts/add_update_farm.html', {'form': form, 'farm': farm})

# Delete Farm (with confirmation page) - only owner can delete
@login_required
def farm_confirm_delete_view(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    if farm.owner != request.user:
        messages.error(request, "You do not have permission to delete this farm.")
        return redirect('farm_detail', pk=farm.pk)
    if request.method == 'POST':
        farm.delete()
        messages.success(request, "Farm deleted successfully!")
        return redirect('survey_home')
    return render(request, 'accounts/farm_confirm_delete.html', {'farm': farm})
