from django.shortcuts import render
from avto.models import Avto
from django.db.models import Count
from django.views.generic import TemplateView
from avto.storage import counter


from django.views import View
import pymongo

class Start(TemplateView):
    template_name = 'avto/index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['counter'] = counter.inc()
        return data

class AvtoView(View):
    def get(self, request):


        client = pymongo.MongoClient(
            "mongodb+srv://AlexUA:IIDS520a@alexua-claster.eulvj.gcp.mongodb.net/<AlexUA-Claster>?retryWrites=true&w=majority")
        db = client.base_avto
        list_avto = db.list_avto
        count = list_avto.count_documents({})

        context = {
            "count": count,

        }
        return render(request, "avto/form.html", context)

    def post(self, request):
        client = pymongo.MongoClient(
            "mongodb+srv://AlexUA:IIDS520a@alexua-claster.eulvj.gcp.mongodb.net/<AlexUA-Claster>?retryWrites=true&w=majority")
        db = client.base_avto
        list_avto = db.list_avto
        nomer_avto = request.POST.get("nomer_avto")
        discript_avto = request.POST.get("discript_avto")
        post = {"nomber": nomer_avto,
                "about": discript_avto
                }
        avto = list_avto.insert_one(post).inserted_id
        print(avto)
        count = list_avto.count_documents({})
        context = {

            "count": count,
        }
        return render(request, "avto/form.html", context)

class Add_avto(View):
    def get(self, request):


        context = {}
        return render(request, "avto/form.html", context)



