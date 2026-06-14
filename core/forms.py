from django import forms

class register(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.TextInput())