from django.shortcuts import render
from .models import Topic

# Create your views here.


def index(request):
    """Home page Learning Log app"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show topic list"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
