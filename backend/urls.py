from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
        path('mark_attendence/', views.mark_attendence),
        path('get_attendence/', views.get_attendence),
        path('get_attendence_dev/', views.get_attendence_dev),
]

urlpatterns = format_suffix_patterns(urlpatterns)
