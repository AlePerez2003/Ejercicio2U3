import csv
from claseSabor import Sabor

class ManejaSabores:
    __sabores: list
    
    def __init__(self):
        self.__sabores = []
        
    def cargar_sabores(self):
        with open('sabores.csv', 'r') as file:
            reader = csv.reader(file, delimiter = ';')
            for fila in reader:
                unSabor = Sabor(int(fila[0]), fila[1], fila[2])
                self.__sabores.append(unSabor)
            print('Los sabores han sido cargados con éxito')
        file.close()
        
    def get_sabores(self):
        return self.__sabores
    
    def get_sabor(self, pos):
        return self.__sabores[pos]
    
    def mostrar_sabores(self):
        for i in range(len(self.__sabores)):
            print('{}: '.format(i+1) + self.__sabores[i].get_nombre())