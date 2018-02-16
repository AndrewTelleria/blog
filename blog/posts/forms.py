from django import forms

from .models import Post, Author

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body',)

class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ('name',)
