from rest_framework import serializers
from .models import Attendence


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = [
            "name",
            "email",
            "isPresent",
            ]


class AttendenceSerializerDev(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = [
            "id",
            "name",
            "email",
            "isPresent",
            "attendence_log",
            ]
