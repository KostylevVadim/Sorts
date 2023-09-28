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
    
class Connection:
    IP = ''
    DB_name = ''
    __instance = None
    
    
    def __new__(cls, ip, db_name):
        if cls.IP == '':
            cls.__instance = super().__new__(cls)
            cls.DB_name = db_name
            cls.IP = ip
            return cls.__instance

        
    
    

    def __str__(self) -> str:
        return 'IP: '+ self.IP + ' DB '+ self.DB_name
        

    

    