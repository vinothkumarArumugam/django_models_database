from django.db import models

# Create your models here.
class student(models.Model):
    student_name=models.CharField(max_length=20)
    student_fees=models.IntegerField()
    student_mark=models.IntegerField()
  #model name student (here it is model)
  # class student which is sub class of models.Model
  # attributes are fields here(which is as column in database)
  
