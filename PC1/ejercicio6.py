## Problema 6:
## Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
## calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
## preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
## años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

# Problema 6: Calculadora de precio de entrada en una sala de juegos

# Solicitar al usuario la edad
edad_cliente = int(input("Ingrese su edad: "))

# Calcular el precio de entrada
if edad_cliente < 4:
    precio_entrada = 0
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar el precio de entrada
print(f'El precio de entrada es: ${precio_entrada}.')