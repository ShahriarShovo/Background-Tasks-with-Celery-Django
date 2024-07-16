from django.forms import ModelForm
from django import forms 
from a_home.models import Message


class MessageCreateform(ModelForm):
    class Meta:
        model = Message
        
        fields =['body']
        widgets = {
            'body' :forms.TextInput(attrs={'placeholder':'Post a message ...', 'class': 'p-4 text-black', 'maxlenght': '2000'}),
        }

