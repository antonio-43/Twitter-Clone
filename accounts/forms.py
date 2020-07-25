from django import forms
from .models import user

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = user
        fields = ['username', 'password']


class ConfirmUser(forms.ModelForm):
    
    class Meta:
        model = user
        fields = ['username', 'password'] 
