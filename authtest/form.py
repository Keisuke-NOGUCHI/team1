from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from accounts.models import Person, TimeTable, Subject

User = get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class Icon(forms.ModelForm):

    class Meta:
        model = Person
        fields = ('icon',) 
        
        
class TimeTableForm(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = "__all__"