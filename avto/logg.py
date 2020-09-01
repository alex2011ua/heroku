
def functionss(func):

    def wrapped(*args, **kwargs):
        print('test logging start')
        print(args[0].user)
        return func(*args, **kwargs)
    return wrapped
