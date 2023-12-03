# main.py
import modulo_operaciones as mo

def menu():
    while True:
        try:
            print("1. Dividir dos números")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                mo.dividir(num1, num2)
            else:
                print("Opción no válida")

        except ValueError:
            print("Error: Ingrese un número válido.")
        else:
            break  # Salir del bucle si no hay excepciones
        finally:
            print("Proceso terminado")

if __name__ == "__main__":
    menu()