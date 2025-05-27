from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SurveillanceRecordForm

def create_surveillancerecord_view(request):
    if request.method == 'POST':
        form = SurveillanceRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Record submitted successfully!")
            return redirect('create_surveillancerecord_view')  # Redirect to clear POST data
    else:
        form = SurveillanceRecordForm()
    return render(request, 'survey/surveillancerecord_form.html', {'form': form})
