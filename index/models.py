from django.db import models


class MyCount(models.Model):
    '''Счетчик показов и другое'''
    stolb = models.CharField(max_length = 20, unique = True)
    m_coun = models.IntegerField()

# Create your models here.
