from rest_framework import serializers
from .models import Attandance

class AttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attandance
        fields = (
            "name",
            "email",
            "isPresent",
            "attandence_Log",
            )
