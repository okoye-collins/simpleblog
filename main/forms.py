from .models import Post
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','tag', 'author', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }