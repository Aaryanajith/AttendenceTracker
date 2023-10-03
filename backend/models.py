from django.db import models
import uuid


def defaultDict():
    return {'log': []}


class Attendence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    attendence_log = models.JSONField(default=defaultDict)
    misc_log = models.JSONField(default=defaultDict)

    def __str__(self):
        return self.email
