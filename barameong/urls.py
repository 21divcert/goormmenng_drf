from django.urls import path
from .views import matchingAIAPIView, CompleteReservationAPIView, FindDogAPIView, DogListAPIView

from django.http import JsonResponse

def ping(request):
    return JsonResponse({"message": "200"}, status=200)

urlpatterns = [
    path('match/', matchingAIAPIView.as_view(), name='match'),
    path('complete/', CompleteReservationAPIView.as_view(), name='reservation'),
    path('find/', FindDogAPIView.as_view(), name='find'),
    path('dog/', DogListAPIView.as_view(), name='dog'),
    path('api/ping/', views.ping, name='ping'),
]