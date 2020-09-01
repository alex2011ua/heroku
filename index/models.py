from django.db import models
from django.conf import settings

class MyCount(models.Model):
    '''Счетчик показов и другое'''
    stolb = models.CharField(max_length = 20, unique = True)
    m_coun = models.IntegerField()

class MyLogg(models.Model):
    date_time = models.DateTimeField(auto_now = True)
    text = models.CharField(max_length = 50)
    context = models.CharField(max_length = 50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                               blank=True, null=True,)

