from django.shortcuts import render
from .forms import message
from .models import  Message

def main(request):
    return render(request, 'main.html')

def contact(request):
    form = message()
    email = None
    text = None
    if request.method == 'POST':
        form = message(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
        Message.objects.create(email=email, text=text)
        
    return render(request,'contact.html',{'form':form})