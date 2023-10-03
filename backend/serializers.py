from rest_framework import serializers
from .models import Attendence


class AttendenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = [
            "name",
            "email",
            "attendence_log",
            "misc_log",
            ]


class AttendenceSerializerDev(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = [
            "id",
            "name",
            "email",
            "attendence_log",
            "misc_log",
            ]
