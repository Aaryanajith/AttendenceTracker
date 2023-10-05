from rest_framework.decorators import api_view, parser_classes
from datetime import datetime
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from .models import Attendee, Event
from .serializers import AttendeeSerializer, EventSerializer
from django.core.exceptions import ObjectDoesNotExist


# expected input format:
# { name: <>, start_date: <>, days: <>, sessions: <> }
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

    return JsonResponse(data, safe=False)
