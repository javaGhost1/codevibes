import email
from django import forms
from .models import Blog, Comment

class TopicForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'tags')
        labels = {'title': '', 'body': '', 'tags': ''}
       
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title of your blog', 'size': '60'}),
            
            'body': forms.Textarea(attrs={'placeholder': 'write down your thoughts', 'rows': '12', 'cols': '60'}),
            'tags': forms.TextInput(attrs={'placeholder': 'academic', 'size': '60'}),

        }

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
        labels = {
            'name': '',
            'email': '',
            'body': ''
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'size': '40'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'size': '40'}),
            'body': forms.Textarea(attrs={'placeholder': 'Your Comment', 'rows': '6', 'cols': '40'}),
        }

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'search-control',
            'placeholder': 'Search...',
            'autocomplete': 'off',
        })
    )
    