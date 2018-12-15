from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'published', 'comment_allowed', 'summary', 'content', 'author']
        widgets = {
            'content': SummernoteWidget(),
        }
