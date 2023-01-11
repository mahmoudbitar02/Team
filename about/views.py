from django.shortcuts import render
from .models import About, Skills, Education, Experience, Service, Projects
from team.models import team1

# Create your views here.

def home (request):
    about = About.objects.last()
    coding_skills= Skills.objects.filter(type='Coding')
    design_skills = Skills.objects.filter(type='Design')
    education=Education.objects.all()
    experience=Experience.objects.all()
    service= Service.objects.all()
    project =Projects.objects.all()
    team = team1.objects.all()

    return render(request, 'index-2.html',{
        'about':about,
        'coding_skill':coding_skills,
        'design_skill':design_skills,
        'education':education,
        'experience':experience,
        'service':service,
        'project':project,
        'team':team

    
    })
