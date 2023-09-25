from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from .models import Attendence
from .serializers import AttendenceSerializer, AttendenceSerializerDev
import csv


"""
mark_attendence():
    Expected input: {'hash': <hash>, 'time': <time>}
    If hash does not exist in db:
        returns 404
    elif isPresent is false:
        set to true and returns 200
    elif isPresent is true:
        attendence_log.append(time) and returns 200
"""


@api_view(['POST'])
@parser_classes([JSONParser])
def mark_attendence(request):

    try:
        hash = request.data['hash']
        time = request.data['time']
    except KeyError:
        response = HttpResponse("Improper input")
        response.status_code = 400
        return response

    try:
        assert (Attendence.objects.filter(id=hash).exists())
    except ValidationError:
        response = HttpResponse("No hash found")
        response.status_code = 404
        return response

    attendence_obj = Attendence.objects.get(id=hash)
    isPresent_value = attendence_obj.isPresent

    if isPresent_value is False:
        attendence_obj.isPresent = True
        attendence_obj.save()
        response = HttpResponse("Marked as present.")
        response.status_code = 200
        return response

    # if isPresent is True
    log = attendence_obj.attendence_log['log']
    log.append(time)
    attendence_obj.save()
    response = HttpResponse("Timestamp appended.")
    response.status_code = 200
    return response


@api_view(['GET'])
def get_attendence(request):
    data = AttendenceSerializer(Attendence.objects.all(), many=True).data
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def get_attendence_dev(request):
    data = AttendenceSerializerDev(Attendence.objects.all(), many=True).data
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendence.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'email', 'isPresent', 'attendence_log'])

    attendence = Attendence.objects.all().values_list(
            'id', 'name', 'email', 'isPresent', 'attendence_log'
            )

    for entry in attendence:
        writer.writerow(entry)

    return response


@api_view(['DELETE'])
def flush_table(request):
    Attendence.objects.all().delete()
    response = HttpResponse("Tables reset.")
    response.status_code = 200
    return response
