from index.models import MyLogg

def functionss(func):

    def wrapped(*args, **kwargs):
        content = args[0].path
        if args[0].POST:
            try:
                content = str(content+args[0].POST.get("nomer_avto"))
            except:
                pass
            try:
                content = str(content + args[0].POST.get("search"))
            except:
                pass
        log = MyLogg.objects.create(text = args[0].user, context = content, user = args[0].user)
        print(content)
        return func(*args, **kwargs)
    return wrapped
