class Counter:

    X = 0

    def __init__(self):
        Counter.X+=1
            

    @classmethod
    def how_much(cls):
        print(cls.X)

class Pizza:
    
    def __init__(self, *args):
        self.__ingr = args[0][:]
    
    @classmethod
    def create_default(cls):
        return Pizza(['chees', 'tomato'])
        
    
    def __str__(self) -> str:
        st = ' '.join(self.__ingr)
        
        return 'Consists of: '+st
    


class Operation:
    @staticmethod
    def sum(a, b):
        return a+b
    @staticmethod
    def dif(a,b):
        return a-b