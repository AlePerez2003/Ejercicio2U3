class Sabor:
    __id: int
    __ingredientes: str
    __nombre: str
    
    def __init__(self, id, ingredientes, nombre):
        self.__id = id
        self.__ingredientes = ingredientes
        self.__nombre = nombre
        
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre