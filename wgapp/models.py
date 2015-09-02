from django.db import models

# Create your models here.


class Flatmate(models.Model):
    short_name = models.CharField(max_length=2)
    full_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.full_name


class Room(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    room = models.ForeignKey(Room)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return ': '.join([self.description, self.room.name])


class Journal(models.Model):
    done_by = models.ForeignKey(Flatmate)
    task = models.ForeignKey(Task)
    done_on = models.DateTimeField('date done')

    def __unicode__(self):
        return ' '.join(self.task, self.done_by, self.done_on)
