from django import forms
from .models import BlogPost

class NewBlog(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ["title", "text"]
