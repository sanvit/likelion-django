from django.shortcuts import render,redirect
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {"blogdata" : blogs})

def postcreate(request):
    if(request.POST['title'] is '' or request.POST['body'] is '' or request.method != 'POST'):
        return render(request, 'none.html')
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')

def postnew(request):
    return render(request, 'create.html')
