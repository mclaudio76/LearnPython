def decorator(arg1):
    def decorator(fun):
        def wrapper(*args,**kwargs):
            print("About to call "+str(fun))
            return fun(*args, **kwargs)
        return wrapper
    return decorator

@decorator("Hello")
def somma(x, y):
    return x+y


print(somma(10,20))