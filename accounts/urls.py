from django.urls import path
from .views import ProfileListCreate

urlpatterns = [
    path('', ProfileListCreate.as_view()),
]
