from django import forms
from .models import Article, Comment

class Image(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('image',)

class Comment_Image(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('image',)