from .storage import counter
from django.views.generic import TemplateView
# Create your views here.

class Start(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        print('start index')
        data = super().get_context_data(**kwargs)

        data['counter'] = counter.inc()
        print(self.request.user)
        return data