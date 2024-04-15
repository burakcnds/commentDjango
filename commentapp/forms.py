from django import forms
from .models import *



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name','text']

        widgets = {
            'full_name' : forms.TextInput(attrs={'class':'form-control w-50 border border-1 border-black m-2'})
        }