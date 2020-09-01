from index.models import MyLogg

def functionss(func):

    def wrapped(*args, **kwargs):
        print('test logging start')
        log = MyLogg.objects.create(text = 'new', context = args[0].user)
        print(args[0].user)
        return func(*args, **kwargs)
    return wrapped
