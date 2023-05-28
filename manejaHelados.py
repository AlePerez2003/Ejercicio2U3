from claseHelado import Helado
from manejaSabores import ManejaSabores

class ManejadoHelados:
    __helados: list
    
    def __init__(self):
        self.__helados = []
        
    def registrar_venta(self, MS:ManejaSabores):
        sabores = []
        print('Ingrese el peso del Helado')
        peso = self.seleccionar_tipo()
        cantidad = int(input('Ingrese la cantidad de sabores que quiere pedir (Entre 1 y 4)'))
        print('Ingrese el ID de el/los sabor/es a pedir')
        MS.mostrar_sabores()
        for i in range(cantidad):
            pos = int(input('Ingrese el ID del {}° sabor'.format(i+1)))
            unSabor = MS.get_sabor(pos-1)
            sabores.append(unSabor)
        precio = self.seleccionar_precio(peso)
        unHelado = Helado(peso, precio, sabores)
        self.__helados.append(unHelado)
        
    def mostrar_tipo(self):
        print('1 - 100gr - $400')
        print('2 - 150gr - $500')
        print('3 - 250gr - $800')
        print('4 - 500gr - $1500')
        print('5 - 1000gr - $2500')
        
    def seleccionar_tipo(self):
        self.mostrar_tipo()
        cod = int(input('Ingrese el codigo del tipo de Helado'))
        if cod == 1:
            peso = 100
        elif cod == 2:
            peso = 150
        elif cod == 3:
            peso = 250
        elif cod == 4:
            peso = 500
        elif cod == 5:
            peso = 1000
        return peso
    
    def seleccionar_precio(self, peso):
        if peso == 100:
            precio = 400
        elif peso == 150:
            precio = 500
        elif peso == 250:
            precio = 800
        elif peso == 500:
            precio = 1500
        elif peso == 1000:
            precio = 2500
        return precio
        
    def contar_pedidos(self, cantS):
        aux = [0 for _ in range(cantS)]
        for vendido in self.__helados:
            for sabor in vendido.get_saboresV():
                aux[sabor.get_id()-1] += 1
        return aux    
                
    def mas_pedidos(self, cantS):
        top5 = []
        pedidos = self.contar_pedidos(cantS)
        for i in range(5):
            max = 0
            pos = 0
            for j in range(len(pedidos)):
                if pedidos[j] > max:
                    max = pedidos[j]
                    pos = j
            pedidos[pos] = 0
            top5.append(pos)
        return top5
            
    def mostrar_mas_pedidos(self, MS:ManejaSabores):
        top5 = self.mas_pedidos(len(MS.get_sabores()))
        sabores = MS.get_sabores()
        print('Estos son los 5 sabores mas pedidos:')
        for ID in top5:
            print(sabores[ID].get_nombre())
            
    def gramos_vendidos(self):
        id = int(input('Ingrese el ID del helado a mostrar los gramos vendidos'))
        total_gramos = 0
        for venta in self.__helados:
            sabores = venta.get_saboresV()
            for sabor in sabores:
                if sabor.get_id() == id:
                    total_gramos += venta.get_gramos() / len(sabores)
        print('El total de gramos vendidos del sabor con ID {} es de {}g'.format(id, total_gramos))
        
    def contar_vendidos_tamaño(self, tamano, cantS):
        aux = [0 for _ in range(cantS)]
        for helado in self.__helados:
            if helado.get_gramos() == tamano:
                for sabor in helado.get_saboresV():
                    aux[sabor.get_id()-1] += 1
        return aux
                    
    def vendidos_tamaño(self,  MS:ManejaSabores):
        tamano = float(input('Ingrese el tamaño del helado'))
        sabores = MS.get_sabores()
        pedidos = self.contar_vendidos_tamaño(tamano, len(sabores))
        print('Estos son los sabores vendidos en el tamaño de {}g'.format(tamano))
        for i in range(len(sabores)):
            if pedidos[i] > 0:
                print('-' + sabores[i].get_nombre())
            
    def calcular_recaudado(self):
        total = [0.0 for _ in range(5)]
        for venta in self.__helados:
            tipo = venta.get_gramos()
            if tipo == 100:
                total[0] += venta.get_precio()
            if tipo == 150:
                total[1] += venta.get_precio()
            if tipo == 250:
                total[2] += venta.get_precio()
            if tipo == 500:
                total[3] += venta.get_precio()
            if tipo == 1000:
                total[4] += venta.get_precio()
        return total
    
    def mostrar_recaudado(self):
        print('Los tipos de helado son los siguientes:')
        self.mostrar_tipo()
        vendido = self.calcular_recaudado()
        for i in range(5):
            print('Recaudad por los helados tipo {} : ${}'.format(i, vendido[i]))
        print('')
            