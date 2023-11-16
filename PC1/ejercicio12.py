## Problema 12:
## La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
## punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
## nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
## como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
## la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
## anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
## la web.
## Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
## archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
## importar el uso de mayúsculas y minúsculas) :
## - .gif
## - .jpg
## - .jpeg
## - .png
## - .pdf
## - .txt
## - .zip
## Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
## ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.

def obtener_tipo_mime(nombre_archivo):
    tipos_mime = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip',
    }

    # Obtener la extensión del archivo
    _, extension = nombre_archivo.rsplit('.', 1) if '.' in nombre_archivo else ('', '')

    # Obtener el tipo de archivo MIME
    return tipos_mime.get('.' + extension.lower(), 'application/octet-stream')

# Ejemplos de uso
archivo1 = 'happy.jpg'
archivo2 = 'document.pdf'

tipo_mime1 = obtener_tipo_mime(archivo1)
tipo_mime2 = obtener_tipo_mime(archivo2)

print(f'Nombre Archivo: {archivo1} - Salida Esperada: {tipo_mime1}')
print(f'Nombre Archivo: {archivo2} - Salida Esperada: {tipo_mime2}')