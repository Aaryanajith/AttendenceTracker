from django.db import models


class Attandance(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    isPresent = models.BooleanField()
    attandence_log = models.JSONField()

    def __str__(self):
        return self.email
