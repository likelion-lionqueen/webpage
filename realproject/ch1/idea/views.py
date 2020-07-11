from django.shortcuts import render
from .models import Idea

# Create your views here.
def idea(request):
    ideas=Idea.objects
    return render(request, 'idea/idea.html',{'idea':ideas})