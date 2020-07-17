from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Course(models.Model):
    university = models.CharField(max_length=300)
    course_code = models.CharField(primary_key=True, max_length=100)
    university_id = models.IntegerField(blank=True,null=True)
    course_title = models.CharField(max_length=500)
    average_score = models.FloatField(blank=True,null=True)
    

    def __str__(self):
        return self.course_code + " " + self.university
    
    class Meta:
        unique_together = ("university_id","course_code")