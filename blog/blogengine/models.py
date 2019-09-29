from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_publish = models.DateTimeField(auto_now_add= True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
