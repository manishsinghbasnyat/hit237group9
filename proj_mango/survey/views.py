from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SurveillanceRecordForm
from .models import SurveillanceRecord, Farm  # <-- Add Farm import

@login_required
def survey_home_view(request):
    user = request.user
    survey_count = SurveillanceRecord.objects.filter(inspector=user).count()
    user_surveys = SurveillanceRecord.objects.filter(inspector=user)
    user_farms = Farm.objects.filter(owner=user)  # Adjust if your user/farm relationship is different
    farm_count = user_farms.count()
    context = {
        'survey_count': survey_count,
        'user_surveys': user_surveys,
        'user_farms': user_farms,
        'farm_count': farm_count,
    }
    return render(request, 'survey/survey_home.html', context)

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
