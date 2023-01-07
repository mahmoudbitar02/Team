from django.db import models

# Create your models here.

class About(models.Model):
    name=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=300)
    image=models.ImageField(upload_to='about/')
    from_adress=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)

    def __str__(self):
        return self.name


SKILL_TYPE =(
    ('Coding','Coding'),
    ('Design','Disign')
)

class Skills(models.Model):
    skill=models.CharField(max_length=100)
    percentage=models.IntegerField()
    type=models.CharField(max_length=15, choices=SKILL_TYPE)

    def __str__(self):
        return self.skill

class Education(models.Model):
    year=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    last=models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Experience(models.Model):
    year=models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    ast=models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Service(models.Model):
    icon=models.CharField(max_length=20)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    def __str__(self):
            return self.title

class Projects(models.Model):
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='projects/')
    tags=models.CharField(max_length=100)
    def __str__(self):
        return self.name
