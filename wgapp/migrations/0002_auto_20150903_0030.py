# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wgapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('done_on', models.DateTimeField(verbose_name=b'date done')),
                ('done_by', models.ForeignKey(to='wgapp.Flatmate')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('room', models.ForeignKey(to='wgapp.Room')),
            ],
        ),
        migrations.RemoveField(
            model_name='taskjournal',
            name='done_by',
        ),
        migrations.RemoveField(
            model_name='taskjournal',
            name='task',
        ),
        migrations.RemoveField(
            model_name='tasklist',
            name='room',
        ),
        migrations.DeleteModel(
            name='TaskJournal',
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
        migrations.AddField(
            model_name='journal',
            name='task',
            field=models.ForeignKey(to='wgapp.Task'),
        ),
    ]
