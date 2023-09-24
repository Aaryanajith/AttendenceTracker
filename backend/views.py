from .models import Attandance
from rest_framework import generics
from .serializers import AttandanceSerializer


class AttandenceList(generics.ListAPIView):
    queryset = Attandance.objects.all()
    serializer_class = AttandanceSerializer
