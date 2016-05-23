from django import forms

from .models import Study, Comment

class StudyForm(forms.ModelForm):

    class Meta:
        model = Study
        fields = ('title', 'abstract', 'inclusions', 'start_date', 'end_date',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)