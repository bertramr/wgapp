
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flatmate/$', views.flatmate_list, name='flatmate_list'),
    url(r'^flatmate/(?P<flatmate_id>[0-9]+)/$', views.flatmate_detail, name='flatmate_detail'),
    url(r'^room/$', views.room_list, name='room_list'),
    url(r'^room/(?P<room_id>[0-9]+)', views.room_detail, name='room_detail'),
    url(r'^task/$', views.task_list, name='task_list'),
    url(r'^task/(?P<task_id>[0-9]+)/', views.task_detail, name='task_detail'),
    url(r'^journal/$', views.journal_list, name='journal_list'),
    url(r'^journal/(?P<journal_id>[0-9]+)/', views.journal_detail, name='journal_detail')
]