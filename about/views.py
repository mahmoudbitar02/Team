from django.shortcuts import render
from .models import About


# Create your views here.

def home (request):
    about = About.objects.last()

    return render(request, 'index-2.html',{
        'about':about
    
    
    })
