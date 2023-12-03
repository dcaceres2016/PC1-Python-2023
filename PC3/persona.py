# persona.py
class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Género: {self.genero}")
