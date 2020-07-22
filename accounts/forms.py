from django import forms
from .models import User

class UserCreationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class ConfirmUser(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password'] 
