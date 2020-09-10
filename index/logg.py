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
            try:
                content += kwargs['nomber']
            except:
                pass
            user_ip = args[0].META.get('HTTP_X_Real_IP')
            if user_ip is None:
                user_ip = args[0].META.get('REMOTE_ADDR')
            content += ' ip:' + user_ip

            log = MyLogg.objects.create(text = text_message, context = content, user = args[0].user)

            return func(*args, **kwargs)
        return wrapped
    return bild_f
