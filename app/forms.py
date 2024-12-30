from django.forms import ModelForm
from .models import Message
from django import forms
class MsgForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'cols':20,'class':'form-control', 'placeholder':'your name'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={'cols':20,'class':'form-control', 'placeholder':'your email'}), label='')
    topic = forms.CharField(widget=forms.TextInput(attrs={'cols':20,'class':'form-control', 'placeholder':'topic you want to discuss'}), label='')
    body = forms.CharField(widget=forms.Textarea(attrs={ 'cols':20,'class':'form-control', 'placeholder':'Your Message'}), label='')
    class Meta:
        model = Message
        fields = '__all__'