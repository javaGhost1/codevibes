import email
from django import forms
from .models import Blog, Comment

<<<<<<< HEAD:blog/forms.py
class TopicForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'tags')
        labels = {'title': '', 'body': '', 'tags': ''}

=======
>>>>>>> d32a961ec6d747a0d677f67036b53b44970dcf36:medium/blog/forms.py
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