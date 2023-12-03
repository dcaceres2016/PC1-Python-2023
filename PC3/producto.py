# producto.py

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        return f"Nombre: {self.nombre}, Código: {self.codigo}"

    def identificar_datos(self):
        pais, lote, anio = self.codigo.split('-')
        print(f"País de origen: {pais}")
        print(f"Número de lote: {lote}")