## Ejercicio 10:

def formato_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    # Verificar si la entrada contiene el formato "Mes dia, año"
    if ',' in fecha:
        mes, dia_anio = fecha.split(' ', 1)
        dia, anio = dia_anio.split(', ')
        mes_numero = meses.index(mes) + 1
    else:
        # Si no, intentar dividir por '/'
        mes, dia, anio = fecha.split('/')
        mes_numero = int(mes)

    # Formatear la fecha en AAAA-MM-DD
    fecha_formateada = f"{anio:04d}-{mes_numero:02d}-{int(dia):02d}"
    return fecha_formateada

entrada_fecha = input("Ingrese la fecha (en formato mes/día/año o Mes día, año): ")
fecha_formateada = formato_fecha(entrada_fecha)
print(f"Fecha formateada: {fecha_formateada}")
