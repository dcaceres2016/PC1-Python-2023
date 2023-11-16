## Problema 9:
## Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
## original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
## 'día', 'buen', 'Di'].

def invertir_lista(lista):
    lista.reverse()

# Ejemplo de uso
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
invertir_lista(lista_original)
print(lista_original)