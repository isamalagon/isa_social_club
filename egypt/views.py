from django.shortcuts import render
from rest_framework import generics
from .models import EgyptTip
from .serializers import EgyptTipSerializer
from django.http import JsonResponse

# show all tips + let me add new ones
class EgyptTipListCreate(generics.ListCreateAPIView):
    queryset = EgyptTip.objects.all()
    serializer_class = EgyptTipSerializer

# little status check just for fun
def egypt_status(request):
    return JsonResponse({
        "message": "welcome from egypt!",
        "tip": "bring water and bring Egyptian currency",
        "vibe": "Egyptian travelers posts"
    })
