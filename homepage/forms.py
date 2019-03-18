from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Announcement

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ['title', 'date_created', 'date_expired', 'summary', 'content', ]
        widgets = {
            'content': SummernoteWidget(),
        }
