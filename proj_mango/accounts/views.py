from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from survey.models import SurveillanceRecord
from accounts.forms import CustomUserCreationForm

# Registration view for new users
def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect('home') 

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # <-- use custom form
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_view')
    else:
        form = CustomUserCreationForm()  # custom form

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')



