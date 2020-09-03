from index.models import MyLogg


def log_decorator(text_message):
    def bild_f(func):
        def wrapped(*args, **kwargs):
            content = str(args[0].user) + ' - '
            if args[0].POST:
                try:
                    content = str(content+args[0].POST.get("nomer_avto"))
                except TypeError as exep:
                    print(str(type(exep)) + 'nomer avto')
                try:
                    content = str(content + args[0].POST.get("search"))
                except TypeError as exep:
                    print(str(type(exep)) + 'search')
            log = MyLogg.objects.create(text = text_message, context = content, user = args[0].user)

            return func(*args, **kwargs)
        return wrapped
    return bild_f
