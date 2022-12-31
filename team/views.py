from django.shortcuts import render, redirect
from .models import team1
from .forms import PostForm

# Create your views here.

def team_list(request):
    all = team1.objects.all()
    return render (request, 'team.html', {'data':all})


def team_detail(request,id):
    team = team1.objects.get(id=id)
    return render (request, 'single.html', {'data':team})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form = PostForm()  

    return render(request,'Create.html', {'form':form})  


def edit(request,id):
    team = team1.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.author = request.user
            myform.save()
    else:
        form = PostForm(instance=team)  

    return render(request,'edit.html', {'form':form}) 

def delete(request,id):
    team = team1.objects.get(id=id)
    team.delete()
    return redirect ('/team')
