# coding: utf8
from django.shortcuts import render
from .models import Diary

def current_tasklist(request):
    if request.method == 'POST':
        temp_data = request.POST
        for i in temp_data:
            if i != 'csrfmiddlewaretoken':
                id = int(i)
        selected = Diary.objects.get(id=id)
        selected.done = True
        selected.save()
    context = {}
    diary_objects = Diary.objects.filter(done=False)
    context['tasklist'] = diary_objects
    template = 'current_tasklist.html'
    return render(request, template, context)

def complete_taslist(request):
    context = {}
    diary_objects = Diary.objects.filter(done=True)
    context['tasklist'] = diary_objects
    template = 'complete_tasklist.html'
    return render(request, template, context)
# Create your views here.
