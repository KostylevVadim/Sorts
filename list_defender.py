class List_Defender():
    def __init__(self, v1):
        self.__v = v1
    
    def __enter__(self):
        self.__copy = self.__v[:]
        return self.__copy
    
    def __exit__(self, exc_type):
        if exc_type is None:
            self.__v = self.__copy[:]
        else:
            print('Ошибочка')
        return False