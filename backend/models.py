from django.db import models
import uuid


def defaultDict():
    return {'log': []}


class Attendence(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attendence_log = models.JSONField(default=defaultDict)
    misc_log = models.JSONField(default=defaultDict)

    def __str__(self):
        return self.email


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    starting_date = models.DateField()
    num_of_days = models.IntegerField()
    num_of_sessions = models.IntegerField()

    def __str__(self):
        return self.name
