from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
        path('mark_attendance/', views.mark_attendence),
]

urlpatterns = format_suffix_patterns(urlpatterns)
