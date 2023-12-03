# main.py
from persona import Persona

def solucion_problema8():
    # Solicitar datos al usuario para instanciar la clase Persona
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    genero = input("Ingrese el género: ")

    # Crear un objeto de la clase Persona con los datos ingresados
    persona = Persona(nombre, edad, genero)

    # Llamar al método para mostrar la información
    persona.mostrar_informacion()

if __name__ == "__main__":
    solucion_problema8()
