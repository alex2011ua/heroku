from django.shortcuts import render
from avto.models import Avto
from django.db.models import Count


from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View





class Add_avto(LoginRequiredMixin, View):
    def get(self, request):
        all_avto = Avto.objects.all().aggregate(count = Count('nomer_avto'))
        context = {
            "count": all_avto['count'],

        }
        return render(request, "avto/form_add.html", context)


    def post(self, request):
        nomer_avto = request.POST.get("nomer_avto").strip()
        discript_avto = request.POST.get("discript_avto")
        avtos = Avto.objects.filter(nomer_avto = nomer_avto)
        all_avto = Avto.objects.all().aggregate(count = Count('nomer_avto'))
        print(len(avtos))
        if len(avtos) == 0:
            Avto.objects.create(nomer_avto=nomer_avto, discript_avto=discript_avto, author = self.request.user)
        context = {

            "count": all_avto['count'],
        }
        return render(request, "avto/form_add.html", context)

class AvtoView(LoginRequiredMixin, View):
    def get(self, request):
        all_avto = Avto.objects.all().aggregate(count = Count('nomer_avto'))
        context = {
            "count": all_avto['count'],

        }
        return render(request, "avto/form_search.html", context)

    def post(self, request):
        nomer_avto = request.POST.get("search").strip()

        avtos = Avto.objects.filter(nomer_avto__icontains = nomer_avto)
        all_avto = Avto.objects.all().aggregate(count = Count('nomer_avto'))
        print(len(avtos))

        context = {
            'zapros': nomer_avto,
            'avtos': avtos,
            "count": all_avto['count'],
            "count_search": len(avtos),
        }
        return render(request, "avto/form_search.html", context)


