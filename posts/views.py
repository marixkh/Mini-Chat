from django.shortcuts import render,redirect
from .forms import new_post
from .models import Post

def posts(request):
    title = None
    content = None
    message = None
    posts = Post.objects.all()

    if request.method == 'POST':
        form = new_post(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post.objects.create(title=title, content=content)
        posts =  Post.objects.all()
        message = 'Good Job ^-^'
    else:
        form = new_post()
    return render(request, 'posts.html',{'title': title, 'content':content, 'form': form, 'message':message, 'posts':posts})

def delete_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect ('posts')

def edit_post(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = new_post(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('posts')
    else:
            form = new_post(initial={
    'title': post.title,
    'content': post.content
})
    return render (request, 'edit_post.html',{'form':form})