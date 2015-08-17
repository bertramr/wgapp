from django.shortcuts import render

from models import TaskJournal, Flatmate


def index(request):
    flatmate_list = Flatmate.objects.all()
    latest_tasks_list = TaskJournal.objects.order_by('-done_on')[:5]
    context = {'latest_tasks_list': latest_tasks_list,
               'flatmate_list': flatmate_list}
    return render(request, 'wgapp/index.html', context)


def detail(request, flatmate_id):
    context = {'flatmate': Flatmate.objects.get(pk=flatmate_id)}
    return render(request, 'wgapp/detail.html', context)
