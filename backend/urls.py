from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
        path('get_attendence/', views.get_attendence),
        path('export/', views.export_csv),
        path('add_session/', views.add_session),
        path('create_event/', views.create_event)
]

urlpatterns = format_suffix_patterns(urlpatterns)
