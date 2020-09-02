from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.


def index(request):
    """
    Home page Learning Log app
    """
    return render(request, 'learning_logs/index.html')


def topics(request):
    """
    Show topic list
    """
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """
    Show one topic and all its entries
    """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """
    Create new topic
    """
    if request.method != 'POST':
        # No data sent; create empty form
        form = TopicForm()
    else:
        # Post data has been sent; process data
        form = TopicForm(data=request.Post)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display empty string or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
