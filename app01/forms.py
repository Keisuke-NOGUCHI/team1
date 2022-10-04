from django import forms
from .models import Article

class Image(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('image',)