from django.db import models
import datetime
import uuid
import json


def defaultDict():
    return {'log': []}


class Attendee(models.Model):
    event_name = models.ForeignKey('Event', on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attendence_log = models.JSONField(default=defaultDict)
    misc_log = models.JSONField(default=defaultDict)

    def __str__(self):
        return self.email

    def save(self, initial, *args, **kwargs):
        if self.event_name and initial:
            attendence_log = dict()
            attendence_log['log'] = []
            event = Event.objects.get(event_name=self.event_name)
            for i in range(event.num_of_days):
                element_dict = dict()
                element_dict['date'] = str(
                        event.starting_date + datetime.timedelta(days=i)
                        )
                for j in range(event.num_of_sessions):
                    element_dict['session' + str(j+1)] = False
                attendence_log['log'].append(element_dict)
            self.attendence_log = attendence_log

        super().save(*args, **kwargs)


class Event(models.Model):
    event_name = models.CharField(
                primary_key=True, max_length=100, unique=True
            )
    starting_date = models.DateField()
    num_of_days = models.IntegerField()
    num_of_sessions = models.IntegerField()

    def __str__(self):
        return self.event_name
