from django.shortcuts import render,redirect,get_object_or_404
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {"blogdata" : blogs})

def postcreate(request):
    if(request.POST['title'] == '' or request.POST['body'] == '' or request.method != 'POST'):
        return render(request, 'none.html')
    if(request.POST.get('not_human', False)):
        return render(request, 'not_human.html')
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
    return redirect('home')

def postnew(request):
    return render(request, 'create.html')

def detail(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'detail.html',{'onepost':onepost})

def postedit(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    return render(request,'postedit.html',{'onepost':onepost})

def postupdate(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    if(request.POST['title'] == '' or request.POST['body'] == '' or request.method != 'POST'):
        return render(request, 'none.html')
    if(request.POST.get('not_human', False)):
        return render(request, 'not_human.html')
    onepost.title = request.POST['title']
    onepost.body = request.POST['body']
    onepost.save()
    return redirect('/detail/'+str(post_id))

def postdelete(request,post_id):
    onepost=get_object_or_404(Blog,pk=post_id)
    onepost.delete()
    return redirect('home')