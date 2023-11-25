## Ejercicio 7:
## Escriba una función de Python que tome un número como parámetro y verifique que el número sea
## primo o no.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = 17  # Puedes cambiar este número para probar
if es_primo(numero):
    print(f"{numero} es primo")
else:
    print(f"{numero} no es primo")
