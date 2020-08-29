from django.shortcuts import render

# Create your views here.


def index(request):
    """Home page Learning Log app"""
    return render(request, 'learning_logs/index.html')
