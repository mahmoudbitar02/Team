from django.shortcuts import render
from .models import team1

# Create your views here.

def team_list(request):
    all = team1.objects.all()
    return render (request, 'team.html', {'data':all})


def team_detail(request,id):
    team = team1.objects.get(id=id)
    return render (request, 'single.html', {'data':team})

def create(request):
    pass


def edit(request):
    pass

def delete(request):
    pass
