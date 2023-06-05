import email
from django import forms
from .models import Comment

class SubcribeForm(forms.Form):
    """Subcription form"""
    email = forms.EmailField()
class EmailPostForm(forms.Form):
    """Build a standard form to share via email"""
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    """Creating dynamic form from comment model"""

    class Meta:
        model = Comment
        fields = ("name", "email", "body")

class SearchForm(forms.Form):
    query = forms.CharField()