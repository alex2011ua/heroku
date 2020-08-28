from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .counts import my_count
from django.views import View
from avto.get_add_avto import add_avto

class Import(LoginRequiredMixin, View):


    @staticmethod
    def get(request):

        context = my_count()
        return render(request, "avto/import.html", context)
    @staticmethod
    def post(request):
        baza = request.FILES.get('image')

        for line in baza:
            content = line.decode('utf-8')
            try:
                nomber, fio, model, diskr = content.split(';')
                add_avto(request, nomber, fio+model+diskr)

            except:
                print(content)



        context = my_count()
        context['content'] = []

        return render(request, "avto/import.html", context)

class Export(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        context = my_count()
        return render(request, "avto/form_search.html", context)

