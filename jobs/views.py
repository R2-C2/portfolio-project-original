from django.shortcuts import render
from .models import Job, Certificate

def home(request):
	context = {
        'jobs': Job.objects.all(),
        'certificates': Certificate.objects.all(),
    }
	return render(request, 'jobs/home.html', context)
