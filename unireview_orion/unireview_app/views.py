
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import CourseSerializer
from rest_framework import generics

# Create your views here.

def home(request):
    return HttpResponse("<h1> Welcome to unireview. Go to http://127.0.0.1:8000/api/Course/ for the database model. </h1>")


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer