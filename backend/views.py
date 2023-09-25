from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from .models import Attendence


# {hash: <>, time: <>}
@api_view(['POST'])
@parser_classes([JSONParser])
def mark_attendence(request):
    hash = request.data['hash']
    time = request.data['time']
    # improve this:
    try:
        if not Attendence.objects.filter(id=hash).exists():
            return Response("UUID not found.")
    except ValidationError:
        return Response("UUID not found.")

    obj = Attendence.objects.get(id=hash)
    isPresent_value = getattr(obj, 'isPresent')
    if isPresent_value is False:
        obj.isPresent = True
        obj.save()
        return Response("200")
    log = obj.attendence_log['log']
    log.append(time)
    obj.save()
    return Response("220")


@api_view(['GET'])
def get_attendence(request):
    data = Attendence.objects.values_list(
            'name', 'email', 'isPresent', 'attendence_log'
            )
    return Response(data)
