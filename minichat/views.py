from django.shortcuts import render,redirect
from .models import Comment
from .forms import register

def mini(request):
    message = None
    form = register()
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            Comment.objects.create(name=name, text=text)
            message = 'Saved!'
    comments = Comment.objects.all()       
    return render(request, 'mini.html', {'message':message, 'form':form, 'comments':comments})
   
def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('mini')

def delete_all(request):
    comment = Comment.objects.all().delete()
    return redirect('mini')
