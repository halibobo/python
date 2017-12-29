def func():
    return 'time'
L = func
print(L.__name__)

def log(func):
    def wrapper(*arg,**kw):
        print('call %s():' % func.__name__)
        return func(*arg,**kw)
    return wrapper

@log
def now():
    return "2019-9-9"
print(now())

def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("注册")
def now():
    print("today")

now()