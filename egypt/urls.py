from django.urls import path
from .views import EgyptTipListCreate, egypt_status

urlpatterns = [
    path('', EgyptTipListCreate.as_view()),
    path('status/', egypt_status),
]
