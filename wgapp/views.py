from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from datetime import date

from models import TaskJournal, Flatmate, Room, TaskList


def index(request):
    flatmate_list = Flatmate.objects.all()
    latest_tasks_list = TaskJournal.objects.order_by('-done_on')[:5]
    context = {'latest_tasks_list': latest_tasks_list,
               'flatmate_list': flatmate_list}
    return render(request, 'wgapp/index.html', context)


def detail(request, flatmate_id):
    context = {'flatmate': Flatmate.objects.get(pk=flatmate_id)}
    return render(request, 'wgapp/detail.html', context)


def room(request):
    room_list = Room.objects.all()
    context = {'room_list': room_list}
    return render(request, 'wgapp/room.html', context)


def room_detail(request, room_id):
    task_list = TaskList.objects.filter(room=room_id).all()
    context = {'task_list': task_list}
    return render(request, 'wgapp/room_detail.html', context)

def choose_flatmate(request, task_id):

    task = get_object_or_404(TaskList, pk=task_id)
    flatmate_list = Flatmate.objects.all()
    context = {'flatmate_list': flatmate_list,
               'task': task}
    try:
        flatmate_id = request.POST['flatmate']
    except (KeyError, Flatmate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'wgapp/choose_flatmate.html', context)
    else:
        tj = TaskJournal()
        tj.task = task
        tj.done_by = Flatmate.objects.get(pk=flatmate_id)
        tj.done_on = date.today()
        tj.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('wgapp:room_detail', args=(task.room.id,)))

