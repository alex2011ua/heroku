from avto.models import MyCount


class Counter:
    key = 'Count_key'

    def __init__(self):
        try:
            self.key = MyCount.objects.get(stolb='count')
        except:
            self.key = MyCount.objects.create(stolb = 'count', m_coun = 0)

    def inc(self):

        self.key.m_coun = self.key.m_coun + 1
        self.key.save()

        return self.key.m_coun


counter = Counter()
