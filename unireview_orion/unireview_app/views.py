
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import permissions, status, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import CourseSerializer, UserSerializer, UserSerializerWithToken, RatingSerializer
from rest_framework import generics

# Create your views here.

def home(request):
    return HttpResponse("<h1> Welcome to unireview. Go to http://127.0.0.1:8000/api/Course/ for the database model. </h1> \n"
     + "<h1> Go to http://127.0.0.1:8000/token-auth/ for the login model. </h1> \n" 
     + "<h1> Go to http://127.0.0.1:8000/users/ for the signup model. </h1> \n" 
     + "<h1> Go to http://127.0.0.1:8000/current_user to use it in front end to display username of current user"
     + "<h1> Go to http://127.0.0.1.8000:/api/Rating for the ratings model")

@api_view(['GET'])
def current_user(request):
    serializer =UserSerializer(request.user)
    return Response(serializer.data)

class UserList(APIView):
    

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    

class RatingViews(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
 