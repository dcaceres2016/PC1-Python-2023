## Problema 5:
## Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
## último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
## verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

# Solicitar al usuario la cantidad de shows musicales vistos en el último año
cantidad_shows = int(input('¿Cuántos shows musicales has visto en el último año?: '))

# Verificar si la cantidad de shows es mayor que 3
verificacion = cantidad_shows > 3

# Mostrar el resultado
print(f'¿Has visto más de 3 shows musicales en el último año?: {verificacion}')