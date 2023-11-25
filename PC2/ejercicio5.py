## Ejercicio 5:
## Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
## Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.

def contar_digitos(numero, digito):
    return str(numero).count(str(digito))

numero = 15789000
digito = 0
cantidad = contar_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}")
