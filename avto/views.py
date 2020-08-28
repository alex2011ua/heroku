from django.shortcuts import render
from avto.models import Avto
from avto.get_add_avto import add_avto, get_avto

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views import View
from .counts import my_count

class AvtoDellConfirm(LoginRequiredMixin, View):
    @staticmethod
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
    def post(request):
        nomer_avto = request.POST.get("nomer_avto").strip()
        discript_avto = request.POST.get("discript_avto")
        avtos = Avto.objects.filter(nomer_avto = nomer_avto)


        if len(avtos) == 0:
            Avto.objects.create(nomer_avto=nomer_avto,
                                discript_avto=discript_avto,
                                author = request.user)
        context = my_count()
        return render(request, "avto/form_add.html", context)


class AvtoView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):

        context = my_count()
        return render(request, "avto/form_search.html", context)

    @staticmethod
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
