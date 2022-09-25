from django import forms
from main.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'tags',
        ]
    
    def clean_tags(self):
        tn = self.cleaned_data.get('tags', [])
        tn = tn[:5]
        return tn

class AnswerForm(forms.Form):
    class Meta:
        model = Answer
        fields = [
            'text'
        ]