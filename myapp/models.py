from django.db import models

# Create your models here.
class Employee(models.Model):  
    eid      = models.CharField(max_length=20)  
    ename    = models.CharField(max_length=100)  
    econtact = models.CharField(max_length=15)  
    class Meta:  
        db_table = "employee" 
 
class Student(models.Model):  
    first_name = models.CharField(max_length=20)  
    last_name  = models.CharField(max_length=30)  
    class Meta:  
        db_table = "student"
  
