from index.models import MyCount


def counter():
    try:
        key = MyCount.objects.get(stolb = 'count')
    except Exception:
        key = MyCount.objects.create(stolb = 'count', m_coun = 0)

    key.m_coun = key.m_coun + 1
    key.save()

    return key.m_coun
