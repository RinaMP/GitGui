from django.db import models


# Create your models here.
class student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_name = models.EmailField(max_length=100)
    phone_name = models.CharField(max_length=100)


class subjects(models.Model):
    first_name = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)
    paper_code = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)
    subjects = models.ForeignKey(student,on_delete=models.DO_NOTHING,default=True)
