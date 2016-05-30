from django import forms
from .models import Study, Comment, UserProfile
from django.utils.translation import ugettext_lazy as _

class StudyForm(forms.ModelForm):

    class Meta:
        model = Study
        fields = ('title', 'abstract', 'inclusions', 'start_date', 'end_date',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class UserProfileForm(forms.ModelForm):

    class Meta:
      model = UserProfile
      fields = ('about','occupation', 'sex', 'age', 'interests')
      labels = {
            "interests": _("Medical Conditions/Interests"),
            "about": _("About Me")
        }