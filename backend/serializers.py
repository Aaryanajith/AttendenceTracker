from rest_framework import serializers
from .models import Attendee, Event


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = [
            "id",
            "name",
            "email",
            "attendence_log",
            "misc_log",
            ]


class EventSerializer(serializers.Serializer):
    event_name = serializers.CharField()
    starting_date = serializers.DateField()
    num_of_days = serializers.IntegerField()
    num_of_sessions = serializers.IntegerField()

    def create(self, validated_data):
        return Event.objects.create(**validated_data)
