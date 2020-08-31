from avto.models import Avto

def add_avto(request, nomer_avto, discript_avto):

    nomer_avto = nomer_avto.strip()
    avtos = Avto.objects.filter(nomer_avto = nomer_avto)

    if len(avtos) == 0:
        Avto.objects.create(nomer_avto = nomer_avto,
                            discript_avto = discript_avto,
                            author = request.user)
def get_avto(request, nomer_avto=False):
    if nomer_avto:
        nomer_avto = nomer_avto.strip()
        avtos = Avto.objects.filter(nomer_avto = nomer_avto)
        return avtos
    avtos = Avto.objects.filter()
    return avtos
