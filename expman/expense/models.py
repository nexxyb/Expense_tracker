from django.db import models

# Create your models here.
class Company(models.Model):
    company_id= models.IntegerField(max_length=4, primary_key=True)
    company_name=models.CharField(max_length=200)
    company_phone=models.IntegerField(max_length=15)
    user_id=models.ForeignKey('User', to_field='user_id', on_delete=models.CASCADE)
    project_id= models.ForeignKey('Project', to_field='project_id', on_delete=models.CASCADE)

class User(models.Model):
    user_id=models.IntegerField(max_length=4, primary_key=True)
    username=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    user_designation=models.CharField(max_length=15)

class Project(models.Model):
    project_id= models.IntegerField(max_length=4, primary_key=True)
    project_name= models.CharField(max_length=30)
    project_amount= models.FloatField(max_length=20)
    start_date=models.DateField()

class Expenses(models.Model):
    expense_id=models.IntegerField(max_length=4, primary_key=True)
    category= models.CharField(max_length=20)
    amount= models.FloatField(max_length=20)
    date=models.DateField()
    staff_id= models.ForeignKey('User', to_field='user_id', on_delete=models.CASCADE)
    project_id= models.ForeignKey('Project', to_field='project_id', on_delete=models.CASCADE)