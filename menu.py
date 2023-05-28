from manejaHelados import ManejadoHelados
from manejaSabores import ManejaSabores

class Menu:
    __cod: int
    
    def __init__(self, cod = 0):
        self.__cod = cod
        
    def mostrar_menu(self):
        print('Opción 1: Cargar sabores')
        print('Opción 2: Registrar venta')
        print('Opción 3: Mostrar el nombre de los 5 sabores de helado más pedidos')
        print('Opción 4: Ingresar un número de sabor y estimar el total de gramos vendidos')
        print('Opción 5: Ingresar por teclado un tipo de helado y mostrar los sabores vendidos en ese tamaño')
        print('Opcion 6: Determinar el importe total recaudado por la Heladería, por cada tipo de helado')
        print('Opción 0: Finalizar operación')
        
    def ejecutar(self, MH:ManejadoHelados, MS:ManejaSabores):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el Código'))
        
        while self.__cod != 0:
            if self.__cod == 1:
                MS.cargar_sabores()
            elif self.__cod == 2:
                MH.registrar_venta(MS)
            elif self.__cod == 3:
                MH.mostrar_mas_pedidos(MS)
            elif self.__cod == 4:
                MH.gramos_vendidos()
            elif self.__cod == 5:
                MH.vendidos_tamaño(MS)
            elif self.__cod == 6:
                MH.mostrar_recaudado()
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el Código'))
            