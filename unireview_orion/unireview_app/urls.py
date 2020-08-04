from django.urls import path
from rest_framework import routers
from . import views
from .views import current_user, UserList



urlpatterns = [
    path('',views.home),
    path('current_user/',current_user),
    path('users/',UserList.as_view()),
]