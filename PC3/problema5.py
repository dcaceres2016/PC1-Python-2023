# main.py
from producto import Producto

def solucion_problema5():
    # Crear un objeto de la clase Producto
    producto = Producto("Pieza de automóvil", "PERU-0001-2023")

    # Imprimir el objeto de forma literal
    print(producto)

    # Identificar país de origen y número de lote
    producto.identificar_datos()

if __name__ == "__main__":
    solucion_problema5()

