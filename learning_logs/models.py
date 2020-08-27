from django.db import models


# Create your models here.

class Topic(models.Model):
    """The topic that user is studying"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string model"""
        return self.text
