from django import forms

class new_post(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.TextInput())
