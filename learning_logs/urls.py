"""URL for learning_logs"""

from django.urls import path
from . import views


app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page with a list of all topics
    path('topics/', views.topics, name='topics'),
    # Page for one topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for add new topic
    path('new_topic/', views.new_topic, name='new_topic')
]
