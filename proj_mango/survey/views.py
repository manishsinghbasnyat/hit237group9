from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SurveillanceRecordForm
from .models import SurveillanceRecord

@login_required
def survey_home_view(request):
    return render(request, 'survey/survey_home.html')

@login_required
def create_surveillancerecord_view(request):
    if request.method == 'POST':
        form = SurveillanceRecordForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            record = form.save(commit=False)
            record.inspector = request.user  # Set inspector to current user
            record.save()
            form.save_m2m()
            messages.success(request, "Record submitted successfully!")
            return redirect('my_surveys_view')  # Redirect to survey list after creation
    else:
        form = SurveillanceRecordForm(user=request.user)
    return render(request, 'survey/surveillancerecord_form.html', {'form': form})

@login_required
def my_surveys_view(request):
    records = SurveillanceRecord.objects.filter(inspector=request.user)
    return render(request, 'survey/my_surveys.html', {'records': records})

@login_required
def survey_detail_view(request, pk):
    record = get_object_or_404(SurveillanceRecord, pk=pk, inspector=request.user)
    return render(request, 'survey/survey_detail.html', {'record': record})
