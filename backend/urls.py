from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
        path('create_event/', views.create_event),
        path('get_events/', views.get_events),
        path('delete_event/', views.delete_event),
        path('get_attendees/', views.get_attendees),
        path('mark_attendence/', views.mark_attendence),
        path('api/jwt/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/jwt/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
