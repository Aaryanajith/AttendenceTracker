from django.db import models
import uuid


class Attendance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    isPresent = models.BooleanField(default=False)
    attandence_log = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.email
