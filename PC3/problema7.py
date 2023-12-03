# main.py
from phone import Phone

def solucion_problema7():
    # Crear un objeto de la clase Phone
    phone = Phone("Samsung", "Galaxy S21", 999.99)

    # Agregar información al nuevo atributo
    phone.color = "Black"

    # Llamar al nuevo método
    phone.mostrar_informacion()

if __name__ == "__main__":
    solucion_problema7()
