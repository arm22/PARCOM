from django.shortcuts import render
from .models import Study

# Create your views here.
def study_list(request):
  studies = Study.objects.all()
  return render(request, 'feed/study_list.html', {'studies': studies})