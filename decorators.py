class Decorators:

    @staticmethod
    def decorator_to_tuple(func):

        def wrapper(a):
        
            a = func(a)
        
            tup = tuple(a)
            return tup
        return wrapper
    @staticmethod
    def decorator_reverse(func):
        def wrapper(a):
            a = func(a)
            return a[::-1]
        return wrapper
    
    @staticmethod
    def set_to_ordered_list(func):
        def wrapper(*args, **kwargs):
            a = func(list(*args))
            return a
        return wrapper
    
    @staticmethod
    def reverse_with_choice(func):
        def wrap(**kwargs):
            if kwargs['choice'] == 1:
                return func(kwargs['list'])
            else:
                return func(kwargs['list'])[::-1]
        return wrap


    

def decorator_to_tuple(func):
    def wrapper(*args, **kwargs):
        a = func(*args, **kwargs)
        tup = tuple(a)
        return tup
    return wrapper 

def reverser(func):
    def wrapper(*args, **kwargs):
        
        a = func(*args, **kwargs)
        return a[::-1]
    return wrapper

def set_to_ordered_list(func):
    def wrapper(*args, **kwargs):
        a = func(list(*args))
        return a
    return wrapper


def reverse_with_choice(func):
    def wrap(**kwargs):
        if kwargs['choice'] == 1:
            return func(kwargs['list'])
        else:
            return func(kwargs['list'])[::-1]
    return wrap