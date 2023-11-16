## Problema 7:
## Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
## - Mostrar una suma de los dos números
## - Mostrar una resta de los dos números (el primero menos el segundo)
## - Mostrar una multiplicación de los dos números
## - En caso de introducir una opción inválida, el programa informará de que no es correcta.

# Solicitar al usuario dos números
num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))

# Mostrar menú
print("Seleccione la operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")

# Solicitar al usuario la opción
opcion = input("Ingrese el número de la operación deseada (1/2/3): ")

# Realizar la operación correspondiente
if opcion == '1':
    resultado = num1 + num2
elif opcion == '2':
    resultado = num1 - num2
elif opcion == '3':
    resultado = num1 * num2
else:
    print("Opción no válida. Por favor, elija 1, 2 o 3.")
    resultado = None

# Mostrar el resultado si es válido
if resultado is not None:
    print(f'Resultado: {int(resultado)}')