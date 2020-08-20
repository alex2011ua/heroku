from django.db import models


class Avto(models.Model):
    nomer_avto = models.CharField(max_length = 10)
    discript_avto = models.CharField(max_length = 1000)


class User(models.Model):
    login = models.CharField(max_length = 20)
    passw = models.CharField(max_length = 20)


class MyCount(models.Model):
    stolb = models.CharField(max_length = 20, unique = True)
    m_coun = models.IntegerField()
