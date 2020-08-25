from django.db import models
from django.conf import settings


class Avto(models.Model):
    ''' таблица автомобилей с описанием '''
    nomer_avto = models.CharField(max_length = 10, unique = True)
    discript_avto = models.CharField(max_length = 1000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                               blank=True, null=True,)


class Topic(models.Model):
    '''Объявления'''
    title = models.CharField(max_length = 50)
    body = models.CharField(max_length = 1000)
    author_topic = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                               blank=True, null=True,)
