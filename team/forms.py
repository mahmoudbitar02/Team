from django import forms
from .models import team1


class PostForm(forms.ModelForm):
    class Meta:
        model = team1
        field = '__all__'
