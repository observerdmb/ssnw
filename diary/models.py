from django.db import models
from django.contrib.auth.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(verbose_name='Задание')
    description = models.TextField(verbose_name='Описание', blank=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    complete_date = models.DateTimeField(auto_now=True, blank=True)
    done = models.BooleanField(editable=False, default=False)

    def __str__(self):
        return self.task
