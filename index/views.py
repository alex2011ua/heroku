from .storage import counter
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from index.logg import log_decorator
from index.models import MyLogg
import os


class Start(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        print('start index')
        data = super().get_context_data(**kwargs)
        data['counter'] = counter()
        return data


class Export(LoginRequiredMixin, TemplateView):
    @staticmethod
    @log_decorator('export')
    def get(request):
        file_name = 'temp_log.xml'
        log = MyLogg.objects.all().order_by('date_time').reverse()[:100]
        with open(file_name, 'w', encoding = 'utf8') as file:
            c = 0
            for logginn in log:
                data = str(logginn.date_time)
                text = logginn.text
                context = logginn.context or ''
                user = str(logginn.user) or ''

                file.write(str(c)+ ". " + data[0:19] + ";" + text + ";" + context + ";" + user + "\n")
                c +=1
        fp = open(file_name, "rb")
        response = HttpResponse(fp.read())
        fp.close()

        file_type = 'application/xml'

        response['Content-Type'] = file_type
        response['Content-Length'] = str(os.stat(file_name).st_size)
        response['Content-Disposition'] = "attachment; filename=report.xml"

        return response
