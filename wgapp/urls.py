
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^flatmate/$', views.FlatmateListView.as_view(), name='flatmate_list'),
    url(r'^flatmate/(?P<pk>[0-9]+)/$', views.FlatmateDetailView.as_view(), name='flatmate_detail'),
    url(r'^room/$', views.RoomListView.as_view(), name='room_list'),
    url(r'^room/(?P<pk>[0-9]+)/$', views.RoomDetailView.as_view(), name='room_detail'),
    url(r'^task/$', views.TaskListView.as_view(), name='task_list'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name='task_detail'),
    url(r'^task/perform/$', views.perform_task, name='perform_task'),
    url(r'^journal/$', views.JournalListView.as_view(), name='journal_list'),
    url(r'^journal/(?P<pk>[0-9]+)/$', views.JournalDetailView.as_view(), name='journal_detail'),
]