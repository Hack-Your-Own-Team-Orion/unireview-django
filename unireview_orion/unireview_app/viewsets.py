from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class CourseViewset(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    

class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter,)
    filter_fields = ('course',)
    search_fields = ('course',)