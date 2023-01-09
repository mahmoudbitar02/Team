from django.shortcuts import render
from .models import About, Skills


# Create your views here.

def home (request):
    about = About.objects.last()
    coding_skills= Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')

    return render(request, 'index-2.html',{
        'about':about,
        'coding_skill':coding_skills,
        'design_skill':design_skills
    
    })
