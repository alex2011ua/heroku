from avto.models import Avto
from django.db.models import Count
from index.storage import counter

def my_count():

    all_avto = Avto.objects.all().aggregate(count = Count('nomer_avto'))
    context = {"count": all_avto['count'],
               }
    context['counter'] = counter.inc()
    return context