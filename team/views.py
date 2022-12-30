from django.shortcuts import render
from .models import team1

# Create your views here.

def team_list(request):
    all = team1.objects.all()
    return render (request, 'team.html', {'data':all})
