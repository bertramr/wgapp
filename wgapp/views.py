from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.views import generic

from datetime import datetime

from models import Journal, Flatmate, Room, Task


class IndexView(generic.ListView):
    template_name = 'wgapp/index.html'

    def get_queryset(self):
        """Return the 5 latest done tasks."""
        return Journal.objects.order_by('-done_on')[:5]


class FlatmateListView(generic.ListView):
    model = Flatmate


class FlatmateDetailView(generic.DetailView):
    model = Flatmate


class TaskListView(generic.ListView):
    model = Task


class TaskDetailView(generic.DetailView):
    model = Task

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(TaskDetailView, self).get_context_data(**kwargs)
        context['latest_done'] = Journal.objects.order_by('-done_on').filter(task=self.object)[:1]
        return context


class RoomListView(generic.ListView):
    model = Room


class RoomDetailView(generic.DetailView):
    model = Room

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        context['task_list'] = Task.objects.filter(room=self.object)
        return context


def perform_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    flatmate_list = Flatmate.objects.all()
    context = {'flatmate_list': flatmate_list,
               'task': task}
    try:
        flatmate_id = request.POST['flatmate']
    except (KeyError, Flatmate.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'wgapp/task_perform.html', context)
    else:
        tj = Journal()
        tj.task = task
        tj.done_by = Flatmate.objects.get(pk=flatmate_id)
        tj.done_on = datetime.now()
        tj.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('wgapp:task_detail', args=(task.id,)))


class JournalListView(generic.ListView):
    model = Journal

    def get_queryset(self):
        return self.model.objects.order_by('-done_on')


class JournalDetailView(generic.DetailView):
    model = Journal


