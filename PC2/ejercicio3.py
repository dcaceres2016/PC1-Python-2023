## Ejercicio 3:
## Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
## ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
## números.
## Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
## números pares e impares.

numeros = []
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == "NO":
        break
    elif respuesta.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print("Números ingresados:", numeros)
print("Cantidad de números pares:", len(pares))
print("Cantidad de números impares:", len(impares))
