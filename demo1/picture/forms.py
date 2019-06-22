from django import forms
from .models import Message


class MessageForm(forms.ModelForm):

    class Meta():
        model = Message
        fields = ['name', 'email', 'phone', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),

        }
