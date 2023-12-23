from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo Task"
        ordering = ["user_id"]
        