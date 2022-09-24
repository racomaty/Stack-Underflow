from django import forms
from main.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'image',
            'tags',
        ]

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))