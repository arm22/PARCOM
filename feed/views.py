from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Study, Comment, UserProfile
from .forms import StudyForm, CommentForm, UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def study_list(request):
  user = request.user
  tags = user.profile.interests.names()
  studies = Study.objects.filter(inclusions__name__in=tags).distinct()
  return render(request, 'feed/study_list.html', {'studies': studies})

@login_required
def study_detail(request, pk):
  study = get_object_or_404(Study, pk=pk)
  tags = study.inclusions.names()
  return render(request, 'feed/study_detail.html', {'study': study, 'tags': tags})

@login_required
def study_new(request):
  if request.method == "POST":
    form = StudyForm(request.POST)
    if form.is_valid():
      study = form.save(commit=False)
      study.author = request.user
      study.published_date = timezone.now()
      study.save()
      return redirect('study_detail', pk=study.pk)
  else:
    form = StudyForm()
  return render(request, 'feed/study_edit.html', {'form': form})

@login_required
def study_edit(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            study = form.save(commit=False)
            study.author = request.user
            study.published_date = timezone.now()
            study.save()
            return redirect('study_detail', pk=study.pk)
    else:
        form = StudyForm(instance=study)
    return render(request, 'feed/study_edit.html', {'form': form})

@login_required
def add_comment_to_study(request, pk):
    study = get_object_or_404(Study, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.study = study
            comment.author = request.user
            comment.save()
            return redirect('feed.views.study_detail', pk=study.pk)
    else:
        form = CommentForm()
    return render(request, 'feed/add_comment_to_study.html', {'form': form})

@login_required
def user_profile(request):
  user = request.user
  if request.method == "POST":
    form = UserProfileForm(request.POST, instance=user.profile)
    if form.is_valid():
      data = form.cleaned_data
      profile = form.save(commit=False)
      user.profile.interests.clear()
      for item in data['interests']:
        user.profile.interests.add(item)
      profile.save()
      return redirect('feed.views.study_list')
  else:
    form = UserProfileForm(instance=user.profile)
  return render(request, 'feed/settings.html', {'form': form})

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    study_pk = comment.study.pk
    comment.delete()
    return redirect('feed.views.study_detail', pk=study_pk)

@login_required
def notifications(request):
  return render(request, 'feed/notifications.html')