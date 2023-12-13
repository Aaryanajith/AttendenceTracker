from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
        path('create_event/', views.create_event),
        path('get_events/', views.get_events),
        path('delete_event/', views.delete_event),
        path('get_attendees/', views.get_attendees),
        path('mark_attendence/', views.mark_attendence),
]

urlpatterns = format_suffix_patterns(urlpatterns)
