from django.shortcuts import render
from .models import Resume

def document(request):
	resumes = Resume.objects
	return render(request, 'resume/document.html', {'resumes':resumes})
