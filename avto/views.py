from django.shortcuts import render
from avto.models import Avto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .counts import my_count
from index.logg import log_decorator
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
import re
from django import forms
from django.http import Http404, HttpResponseNotModified


class FormAdd(forms.Form):



class AvtoDellConfirm(LoginRequiredMixin, View):
    @staticmethod
    @log_decorator('Удаление авто')
    def get(request, nomber,):
        count = my_count()
        avto = Avto.objects.get(nomer_avto = nomber)
        context = {
            'nomer': nomber,
            'discr': avto.discript_avto
        }
        context.update(count)
        avto.delete()
        return render(request, "avto/form_dell_confirm.html", context)


class AvtoDell(LoginRequiredMixin, View):
    @staticmethod
    def get(request, nomber, ):
        print(nomber)
        print(request.user.username)
        avto = Avto.objects.get(nomer_avto = nomber)
        context = {
            'nomer': nomber,
            'discr': avto.discript_avto
        }
        return render(request, "avto/form_dell.html", context)


class AddAvto(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = my_count()
        return render(request, "avto/form_add.html", context)

    @staticmethod
    @log_decorator('Добавление авто')
    def post(request):
        nomer_avto = request.POST.get("nomer_avto").strip()
        nomer_avto = nomer_avto.replace(' ', '')
        pattern = r'^\w+$'
        if not re.match(pattern, nomer_avto):
            context = {
                'url': reverse('add'),
                'text_error': 'Ошибка! Номер введен не верно!'
            }
            return render(request, "message.html", context)
        discript_avto = request.POST.get("discript_avto")
        try:
            avto = Avto.objects.get(nomer_avto=nomer_avto)
            avto.discript_avto = discript_avto
            avto.author = request.user
            avto.save()
        except ObjectDoesNotExist:
            avto = Avto.objects.create(
                nomer_avto = nomer_avto,
                discript_avto = discript_avto,
                author = request.user)
        context = my_count()
        return HttpResponseRedirect(reverse('view'))


class AvtoView(LoginRequiredMixin, View):

    @staticmethod
    def get(request):
        context = my_count()
        print(reverse('view'))
        return render(request, "avto/form_search.html", context)

    @staticmethod
    @log_decorator('Показ запроса')
    def post(request):
        context = my_count()
        nomer_avto = request.POST.get("search").strip()
        avtos = Avto.objects.filter(nomer_avto__icontains = nomer_avto)
        context.update({
            'zapros': nomer_avto,
            'avtos': avtos,
            "count_search": len(avtos),
        })
        return render(request, "avto/form_search.html", context)
