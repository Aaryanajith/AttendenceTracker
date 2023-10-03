from rest_framework.decorators import api_view, parser_classes
import datetime
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse
from .models import Attendence
from .serializers import AttendenceSerializer, AttendenceSerializerDev
import csv

attendence_log_template = dict()


# @api_view(['POST'])
# @parser_classes([JSONParser])
# def mark_attendence(request):

# expected input: 
# { name: <>, start_date: <>, days: <>, sessions: <> }
@api_view(['POST'])
@parser_classes([JSONParser])
def create_event(request):
    reponse = HttpResponse()

    
@api_view(['GET'])
def get_attendence(request):
    data = AttendenceSerializer(Attendence.objects.all(), many=True).data
    return JsonResponse(data, safe=False)


# Debugging purposes
@api_view(['GET'])
def get_attendence_dev(request):
    data = AttendenceSerializerDev(Attendence.objects.all(), many=True).data
    return JsonResponse(data, safe=False)


@api_view(['GET'])
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendence.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'id', 'name', 'email', 'isPresent', 'attendence_log', 'misc_log'
        ])

    attendence = Attendence.objects.all().values_list(
            'id', 'name', 'email', 'isPresent', 'attendence_log', 'misc_log'
            )

    for entry in attendence:
        writer.writerow(entry)

    return response


# Expected input:
# { date:, days:, sessions: }
@api_view(['POST'])
@parser_classes([JSONParser])
def add_session(request):
    attendence_log_template['log'] = []
    for i in range(request.data['days']):
        element_dict = dict()
        date = datetime.datetime.strptime(request.data['date'], '%d/%m/%Y')
        element_dict['date'] = str(date + datetime.timedelta(days=i))
        for j in range(request.data['sessions']):
            element_dict['session' + str(j+1)] = False
        attendence_log_template['log'].append(element_dict)
    Attendence.objects.all().update(attendence_log=attendence_log_template)
    return HttpResponse(attendence_log_template.items())
