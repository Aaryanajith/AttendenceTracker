from django.db import models
import datetime


def defaultDict():
    return {'log': []}


class Attendee(models.Model):
    event_name = models.ForeignKey('Event', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    roll_number = models.CharField(max_length=150, null=True, blank=True)
    attendence_log = models.JSONField(default=defaultDict)
    misc_log = models.JSONField(default=defaultDict)

    def __str__(self):
        return self.email

    def save(self, initial=True, *args, **kwargs):
        if self.event_name and initial:
            attendence_log = dict()
            attendence_log['log'] = []
            event = Event.objects.get(event_name=self.event_name)

            for i in range(event.num_of_days):
                day_element = dict()
                day_element['date'] = str(event.starting_date
                                          + datetime.timedelta(days=i))

                for j in range(event.num_of_sessions):
                    day_element['session' + str(j+1)] = False

                attendence_log['log'].append(day_element)

            self.attendence_log = attendence_log

        super().save(*args, **kwargs)


class Event(models.Model):
    event_name = models.CharField(primary_key=True,
                                  max_length=100,
                                  unique=True)
    starting_date = models.DateField()
    num_of_days = models.IntegerField()
    num_of_sessions = models.IntegerField()

    def __str__(self):
        return self.event_name
