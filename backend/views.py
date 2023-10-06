from rest_framework.decorators import api_view, parser_classes, authentication_classes
from datetime import datetime
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from .models import Attendee, Event
from .serializers import AttendeeSerializer, EventSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt import authentication

"""
API Documentation

create_event() :
    input: {
            event_name: "",
            starting_date: "",
            num_of_days: uint,
            num_of_sessions: uint,
        }
    output:
        if input is in incorrect format: {}, 400
        else if serializer is not valid: {serializer.error}, 400
        else: {input data}, 201

get_events():
    output: [All events as JSON], 200

delete_events():
    input: {
            event_name : "",
        }
    output:
        if event does not exist: 404
        else: 200

get_attendees():
    [POST only] input: {
                    event_name = ""
                }
    output: [All attendees for that event in JSON], 200

mark_attendence():
    input: {
            date: "",
            time: "",
            session: "",
            id: "",
    }
"""


@api_view(['POST'])
@parser_classes([JSONParser])
def create_event(request):

    try:
        request.data['starting_date'] = datetime.strptime(
            request.data['starting_date'], "%d/%m/%Y"
        ).date()
    except (KeyError, ValueError):
        return JsonResponse(status=400)

    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(['GET'])
def get_events(request):
    data = EventSerializer(Event.objects.all(), many=True).data
    return JsonResponse(data, safe=False, status=200)


@api_view(['DELETE'])
@parser_classes([JSONParser])
def delete_event(request):
    try:
        event = Event.objects.get(event_name=request.data['event_name'])
        event.delete()
        return HttpResponse(status=200)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)


@api_view(['GET', 'POST'])
def get_attendees(request):
    if request.method == 'GET':
        data = AttendeeSerializer(Attendee.objects.all(), many=True).data

    if request.method == 'POST':
        data = AttendeeSerializer(Attendee.objects.filter(
            event_name=request.data['event_name']), many=True
        ).data

    return JsonResponse(data, safe=False, status=200)


@api_view(['POST'])
@parser_classes([JSONParser])
def mark_attendence(request):
    try:
        attendee = Attendee.objects.get(id=request.data['id'])
        date = datetime.strptime(request.data['date'], "%d/%m/%Y").date()

        for day in attendee.attendence_log['log']:
            if day['date'] == str(date):  # find matching date dict

                # if attendence on that day for that session is already true
                # append time to misc_log
                if day[request.data['session']]:
                    attendee.misc_log['log'].append(request.data['time'])
                    attendee.save(initial=False)
                    return HttpResponse(status=201)

                # else set attendence for session to true
                day[request.data['session']] = True
                attendee.save(initial=False)
                return HttpResponse(status=201)

        # could not find day (invalid date)
        return HttpResponse(status=404)

    except (ObjectDoesNotExist, ValueError):
        return HttpResponse(status=404)
