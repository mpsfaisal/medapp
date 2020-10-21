from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class patient_details(models.Model):
      genders = (('M','Male'),('F','Female'),('O','Others'))
      name = models.CharField(max_length=30)
      phone=models.CharField(max_length=10)
      address = models.TextField()
      gender = models.CharField(max_length=10, choices=genders)
      consulting_date = models.DateField()
      history = models.TextField()
      observations = models.TextField()
      remedy = models.TextField()
      next_consultation = models.DateField()
      entry_by = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
      
      def __str__(self):
          return (self.name)

