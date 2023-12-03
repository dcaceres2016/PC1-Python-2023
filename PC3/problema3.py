# main.py
from catalogo import Catalogo, Producto

def solucion_problema3():
    # Crear un objeto de la clase Catalogo
    catalogo = Catalogo()

    # Agregar productos al catálogo
    producto1 = Producto("Filtro de aceite", 15.99)
    producto2 = Producto("Pastillas de freno", 29.99)
    producto3 = Producto("Batería de coche", 89.99)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar la lista de productos en el catálogo
    print("Lista de productos en el catálogo:")
    catalogo.mostrar_productos()

if __name__ == "__main__":
    solucion_problema3()
