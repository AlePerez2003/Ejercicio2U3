class Helado:
    __gramos: float
    __precio: float
    __saboresV: list
    
    def __init__(self, gramos, precio, sabores):
        self.__gramos = gramos
        self.__precio = precio
        self.__saboresV = sabores
        
    def get_saboresV(self):
        return self.__saboresV
    
    def get_gramos(self):
        return self.__gramos
    
    def get_precio(self):
        return self.__precio