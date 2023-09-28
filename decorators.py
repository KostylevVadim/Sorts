class Decorators:
    
    @staticmethod
    def decorator_to_tuple(func):

        def wrapper(a):
        
            a = func(a)
        #a = reversed(a)
            tup = tuple(a)
            return tup
        return wrapper
    @staticmethod
    def decorator_reverse(func):
        def wrapper(a):
            a = func(a)
            return a[::-1]
        return wrapper

def decorator(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        tup = tuple(a)
        return tup
    return wrapper 

