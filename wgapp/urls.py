
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<flatmate_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^room/$', views.room, name='room'),
    url(r'^room/(?P<room_id>[0-9]+)', views.room_detail, name='room_detail'),
    url(r'^task/(?P<task_id>[0-9]+)/', views.choose_flatmate, name='choose_flatmate')
]