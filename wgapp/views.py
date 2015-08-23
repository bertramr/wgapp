from django.shortcuts import render

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
    flatmate_list = Flatmate.objects.all()
    task = TaskList.objects.get(pk=task_id)
    context = {'flatmate_list': flatmate_list,
               'task': task}
    return render(request, 'wgapp/choose_flatmate.html', context)