from django.shortcuts import render, get_object_or_404
from .models import Study

# Create your views here.
def study_list(request):
  studys = Study.objects.all()
  return render(request, 'feed/study_list.html', {'studys': studys})

def study_detail(request, pk):
  study = get_object_or_404(Study, pk=pk)
  return render(request, 'feed/study_detail.html', {'study': study})