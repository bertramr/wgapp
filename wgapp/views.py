from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from datetime import datetime

from models import TaskJournal, Flatmate, Room, TaskList


def index(request):
    latest_tasks_list = TaskJournal.objects.order_by('-done_on')[:5]
    context = {'latest_tasks_list': latest_tasks_list}
    return render(request, 'wgapp/index.html', context)


def flatmate_list(request):
    context = {'flatmate_list': Flatmate.objects.all()}
    return render(request, 'wgapp/flatmate_list.html', context)


def flatmate_detail(request, flatmate_id):
    context = {'flatmate': Flatmate.objects.get(pk=flatmate_id)}
    return render(request, 'wgapp/flatmate_detail.html', context)


def task_list(request):
    context = {'task_list': TaskList.objects.all()}
    return render(request, 'wgapp/task_list.html', context)


def room_list(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'wgapp/room_list.html', context)


def room_detail(request, room_id):
    room = Room.objects.get(pk=room_id)
    task_list = TaskList.objects.filter(room=room_id).all()
    context = {'task_list': task_list,
               'room': room}
    return render(request, 'wgapp/room_detail.html', context)


def task_detail(request, task_id):

    task = get_object_or_404(TaskList, pk=task_id)
    flatmate_list = Flatmate.objects.all()
    context = {'flatmate_list': flatmate_list,
               'task': task}
    try:
        flatmate_id = request.POST['flatmate']
    except (KeyError, Flatmate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'wgapp/task_detail.html', context)
    else:
        tj = TaskJournal()
        tj.task = task
        tj.done_by = Flatmate.objects.get(pk=flatmate_id)
        tj.done_on = datetime.now()
        tj.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('wgapp:room_detail', args=(task.room.id,)))


def journal_list(request):
    context = {'journal_list': TaskJournal.objects.all()}
    return render(request, 'wgapp/journal_list.html', context)


def journal_detail(request, journal_id):
    context = {'journal': TaskJournal.objects.get(pk=journal_id)}
    return render(request, 'wgapp/journal_detail.html', context)
