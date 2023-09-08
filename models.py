from django.db import models

# Create your models here.
class employee(models.Model):
    empoyee_no=models.IntegerField()
    employee_name=models.CharField(max_length=20)
    employee_salary=models.IntegerField()
    employee_adress=models.CharField(max_length=200)
  #model name employeee (here it is model)
  # class employee which is sub class of models.Model
  # attributes are fields here(which is as column in database)
  
