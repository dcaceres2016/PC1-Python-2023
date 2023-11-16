## Problema 4:
## Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
## pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
## puede ser calculada de la siguiente forma:

N=int(input('Ingrese numero entero positivo: '))  

# Validar que N sea un entero positivo
if N <= 0:
    print('Por favor, ingrese un entero positivo.')
else:
    # Calcular la suma de todos los enteros desde 1 hasta N
    suma_total = (N*(N+1))/2

    # Mostrar el resultado
    print(f'La suma de todos los enteros desde 1 hasta {N} es: {int(suma_total)}')