# main.py
from circulo import Circulo

def solucion_problema2():
    # Crear un objeto de la clase Circulo con radio 5
    circulo = Circulo(5)

    # Calcular y mostrar el área
    area = circulo.calcular_area()
    print(f"Área del círculo con radio {circulo.radio}: {area}")

if __name__ == "__main__":
    solucion_problema2()