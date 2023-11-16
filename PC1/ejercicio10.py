## Problema 10:
## Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
## encuentran en la posición 0, 4 y 5.
## lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
## Resultado esperado: ['Verde', 'Blanco', 'Negro']

def eliminar_elementos(lista, posiciones):
    for posicion in sorted(posiciones, reverse=True):
        try:
            lista.pop(posicion)
        except IndexError:
            pass

# Lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
posiciones_eliminar = [0, 4, 5]

# Resultado esperado
eliminar_elementos(lista_muestra, posiciones_eliminar)
print(lista_muestra)