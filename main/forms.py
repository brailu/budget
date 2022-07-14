from unicodedata import name
from django import forms
from main.models import (
    Account,
    Category, 
)

class CategoryCreateForm(forms.ModelForm):
    pass


class AccountCreateForm(forms.ModelForm):
    
    class Meta():
        model = Account
        fields = ['name', 'type', 'balance']


class AccountUpdateForm(forms.ModelForm):
    
    class Meta():
        model = Account
        fields = ['name']
