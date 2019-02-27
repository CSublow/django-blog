from django import forms # Import the django forms library
from .models import Post # Import the post class you created in models.py

class BlogPostForm(forms.ModelForm): # Create a form for creating blog posts using django's form library
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'tag', 'published_date') # You only want fields on your form that the user can actually edit