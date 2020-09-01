from django.db import models


class MyCount(models.Model):
    '''Счетчик показов и другое'''
    stolb = models.CharField(max_length = 20, unique = True)
    m_coun = models.IntegerField()

class MyLogg(models.Model):
    date_time = models.DateTimeField(auto_now = True)
    text = models.CharField(max_length = 50)
    context = models.CharField(max_length = 50)
# Create your models here.
