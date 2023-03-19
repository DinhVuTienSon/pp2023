class Uni:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
class Students(Uni):
    def __init__(self, name, id, DoB):
        super().__init__(name, id)
        self.__DoB = DoB
        
    def get_DoB(self):
        return self.__DoB

class Courses(Uni):
    def __init__(self, name, id):
        super().__init__(name, id)