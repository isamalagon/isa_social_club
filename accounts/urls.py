from django.urls import path
from . import login
from . import profile

urlpatterns = [
    path("login/", login.login),
    path("profile/", profile.profile),
]
