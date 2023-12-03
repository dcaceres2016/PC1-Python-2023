# modulo_operaciones.py
import os

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado de la división: {resultado}")
        print(f"Directorio actual: {os.getcwd()}")
    finally:
        print("Proceso terminado")