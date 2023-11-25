## Ejercicio 8:
## Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
## función acepta el número como argumento.

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

numero = 5  # Puedes cambiar este número para probar
resultado = factorial(numero)
print(f"El factorial de {numero} es {resultado}")
