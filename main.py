from pyfiglet import Figlet
import random
import requests
from datetime import datetime
import modulos.bd as bd
from modulos.proceso import *

database = None

def mostrar_menu():
    print("Bienvenidos a store DatuxTec")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Editar nombre de producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("6. Editar precio o stock")  # Nueva opción
    print("7. Buscar producto por nombre")  # Nueva opción
    print("8. Agregar cliente")  # Nueva opción
    print("9. Listar clientes")  # Nueva opción
    print("2.1 Editar título del menú usando pyfiglet")

def bienvenido():
    bienvenida_texto = "¡Bienvenido al programa!"
    print(pyfiglet.figlet_format(bienvenida_texto))

def opcion_2_1():
    nuevo_titulo = input("Ingrese el nuevo título del menú: ")
    fuentes_disponibles = Figlet().getFonts()
    fuente_seleccionada = random.choice(fuentes_disponibles)
    figlet = Figlet(font=fuente_seleccionada)
    titulo_formateado = figlet.renderText(nuevo_titulo)
    print(f"\nNuevo título del menú con fuente '{fuente_seleccionada}':\n{titulo_formateado}")

def editar_precio_stock(user):
    # TODO: Lógica para editar precio o stock
    pass

def buscar_producto_por_nombre(user):
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")
    # TODO: Lógica para buscar producto por nombre
    pass

def agregar_cliente(user):
    # TODO: Lógica para agregar un cliente
    pass

def listar_cliente(user):
    # TODO: Lógica para listar clientes
    pass

def actualizar_tipo_cambio(database):
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        valor_cambio = data.get('venta', 0.0)  # Ajusta esto según la estructura de la API

        query_insert = f"INSERT INTO tipo_cambio (fecha, valor_cambio) VALUES ('{fecha_actual}', {valor_cambio});"
        database.execute_query(query_insert)
        print("Tipo de cambio actualizado correctamente.")
    else:
        print("Error al obtener el tipo de cambio desde la API.")

def config():
    global database
    database = bd.Bd()

    query_products = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        );
    """
    database.execute_query(query_products)

    query_tipo_cambio = """
        CREATE TABLE IF NOT EXISTS tipo_cambio (
            id INTEGER PRIMARY KEY,
            fecha DATE NOT NULL,
            valor_cambio REAL NOT NULL
        );
    """
    database.execute_query(query_tipo_cambio)

    query_cliente = """
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            direccion VARCHAR(200) NOT NULL,
            telefono VARCHAR(15) NOT NULL
        );
    """
    database.execute_query(query_cliente)

if __name__ == '__main__':
    bienvenido()
    config()
    main()