from manejaHelados import ManejadoHelados
from manejaSabores import ManejaSabores
from menu import Menu

if __name__ == '__main__':
    MH = ManejadoHelados()
    MS = ManejaSabores()
    menu = Menu()
    menu.ejecutar(MH, MS)