from django import forms

class register(forms.Form):
    name = forms.CharField()
    text = forms.CharField(widget=forms.TextInput())

class new_post(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.TextInput())

class message(forms.Form):
    email = forms.EmailField()
    text = forms.CharField(widget=forms.TextInput())