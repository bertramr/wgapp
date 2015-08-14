from django.db import models

# Create your models here.


class Flatmate(models.Model):
    short_name = models.CharField(max_length=2)
    full_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.full_name


class TaskList(models.Model):
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description

class TaskJournal(models.Model):
    done_by = models.ForeignKey(Flatmate)
    task = models.ForeignKey(TaskList)
    done_on = models.DateTimeField('date done')
