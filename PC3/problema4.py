# main.py
import operaciones
import os

def menu():
    while True:
        try:
            print("1. Dividir dos números")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                resultado = operaciones.dividir(num1, num2)
                print(f"Resultado: {resultado}")
            else:
                print("Opción no válida")

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            print(f"Directorio actual: {os.getcwd()}")
        finally:
            print("Proceso terminado")

if __name__ == "__main__":
    menu()
