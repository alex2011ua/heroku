from index.models import MyCount


class Counter:
    key = 'Count_key'

    def __init__(self):
        print('init counter')
        try:
            print('try get count')
            self.key = MyCount.objects.get(stolb='count')

        except:
            print('exept, create count')
            self.key = MyCount.objects.create(stolb = 'count', m_coun = 0)

    def inc(self):
        print('inc')
        self.key.m_coun = self.key.m_coun + 1
        self.key.save()

        return self.key.m_coun

print('make counter')
#counter = Counter()
