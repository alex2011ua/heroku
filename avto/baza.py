from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .counts import my_count
from django.views import View
from avto.get_add_avto import add_avto, get_avto
from django.http import HttpResponse
import os
import mimetypes
from index.logg import log_decorator

class Import(LoginRequiredMixin, View):

    @staticmethod
    def get(request):

        context = my_count()
        return render(request, "avto/import.html", context)

    @staticmethod
    @log_decorator('Импорт базы')
    def post(request):
        baza = request.FILES.get('image')

        for line in baza:
            content = line.decode('utf-8')
            try:
                nomber, fio, model, diskr = content.split(';')
                add_avto(request, nomber, (fio+model+diskr).strip())

            except Exception:
                try:
                    nomber, diskr = content.split(';')
                    add_avto(request, nomber, (diskr).strip())
                except Exception:
                    print(Exception)



        context = my_count()
        context['content'] = []

        return render(request, "avto/import.html", context)

class Export(LoginRequiredMixin, View):
    @staticmethod
    @log_decorator('Экспорт базы')
    def get(request):
        file_name = 'temp.xml'
        with open(file_name, 'w', encoding = 'utf8') as file:
            for avto in get_avto(request):
                file.write(avto.nomer_avto + ";" + avto.discript_avto + '\n')



        fp = open(file_name, "rb")
        response = HttpResponse(fp.read())
        fp.close()

        file_type = mimetypes.guess_type(file_name, strict=False)

        file_type = 'application/xml'

        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(file_name).st_size)
        response['Content-Disposition'] = "attachment; filename=report.xml"


        return response




