## Ejercicio 4:
## Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
## pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
## materias.
## Puede usar el siguiente esquema a manera de ejemplo
## {
## Alumno: Juan,
## Notas: [10, 12, 15]
## }
## Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
## completo de los alumnos.
## Nota:
## El uso de listas con diccionarios le será de utilidad.

def ingresar_alumnos():
    alumnos = []
    n = int(input("Ingrese la cantidad de alumnos: "))
    
    for _ in range(n):
        nombre = input("Ingrese el nombre del alumno: ")
        notas = [float(input(f"Ingrese la nota {i + 1} del alumno {nombre}: ")) for i in range(3)]
        alumno = {"Alumno": nombre, "Notas": notas}
        alumnos.append(alumno)

    return alumnos

def mostrar_alumnos(alumnos):
    for alumno in alumnos:
        print(alumno)

alumnos = ingresar_alumnos()
mostrar_alumnos(alumnos)
