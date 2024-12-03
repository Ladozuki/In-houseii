from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    file = models.FileField(upload_to='tasks/', blank=True, null=True)

    def __str__(self):
        return self.title
