from django import forms

class TodoForm(forms.Form):
    title = forms.CharField()
    completed = forms.BooleanField()