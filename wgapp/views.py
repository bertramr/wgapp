from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import TaskJournal

def index(request):
    latest_tasks_list = TaskJournal.objects.order_by('-done_on')[:5]
    context = {'latest_tasks_list': latest_tasks_list}
    return render(request, 'wgapp/index.html', context)