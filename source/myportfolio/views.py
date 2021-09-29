from django.shortcuts import render
from .models import project


def home(request):
    proj = project.objects.all()
    context = {
        "projects": proj
    }
    return render(request, "home.html", context)
