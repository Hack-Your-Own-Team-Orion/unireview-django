from django.db import models
from django.contrib.postgres.fields import ArrayField
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
    

    def __str__(self):
        return self.course_code + " " + self.university
    
    class Meta:
        unique_together = ("university_id","course_code")

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created = False, **kwargs):
    if created:
        Token.objects.create(user=instance)