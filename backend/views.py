from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.core.exceptions import ValidationError
from .models import Attendance


# {hash: <>, time: <>}
@api_view(['POST'])
@parser_classes([JSONParser])
def mark_attendence(request):
    hash = request.data['hash']
    # improve this:
    try:
        if not Attendance.objects.filter(id=hash).exists():
            return Response("no")
    except ValidationError:
        return Response("no")
    return Response("yes")
