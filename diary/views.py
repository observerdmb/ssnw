from django.shortcuts import render
from .models import Diary

def current_tasklist(request):
    context = {}
    diary_objects = Diary.objects.filter(done=False)
    context['tasklist'] = diary_objects
    template = 'current_tasklist.html'
    return render(request, template, context)

# Create your views here.
