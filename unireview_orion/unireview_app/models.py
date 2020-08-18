from django.db import models
from django.db.models import Avg
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Course(models.Model):
    university = models.CharField(max_length=300)
    course_code = models.CharField(primary_key=True, max_length=100)
    university_id = models.IntegerField(blank=True,null=True)
    course_title = models.CharField(max_length=500)
    average_score = models.FloatField(blank=True,null=True)

  
    def avg_enjoyability(self):
        average_enjoyability = Rating.objects.filter(course=self).aggregate(Avg('enjoyability'))
        return average_enjoyability
    
    def avg_difficulty(self):
        average_difficulty = Rating.objects.filter(course=self).aggregate(Avg('difficulty'))
        return average_difficulty

    def avg_usefulness(self):
        average_usefulness = Rating.objects.filter(course=self).aggregate(Avg('usefulness'))
        return average_usefulness
    
    def avg_overall_rating(self):
        average_overall_rating = Rating.objects.filter(course=self).aggregate(Avg('overall_rating'))
        return average_overall_rating
    

    def __str__(self):
        return self.course_code + " " + self.university
    
    class Meta:
        unique_together = ("university_id","course_code")

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    username_id = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length = 400)
    time_submitted = models.DateTimeField(auto_now=True)
    professor = models.CharField(max_length = 50)
    enjoyability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    difficulty = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    usefulness = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    overall_rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('username_id','course'),)
        index_together = (('username_id','course'),)





@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)