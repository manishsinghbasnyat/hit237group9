from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already registered and logged in.")
        return redirect('home')  # or wherever you want to redirect logged-in users

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('login_view')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
