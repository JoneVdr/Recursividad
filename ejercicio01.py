#El capítulo «Iteración» ha resuelto el problema definiendo una función iterativa.
#Ejercicio resuelto 5: Búsqueda recursiva por dicotomía en una tabla ordenada
#Se pide resolver el mismo problema definiendo una función recursiva.
#Puede encontrar una solución estudiada de este ejercicio en los complementos disponibles para descargar desde la página Información.

def dicotomia(lista, valor):
    if len(lista) == 0:
        return False
    else:
        mitad = len(lista) // 2
        if lista[mitad] == valor:
            return True
        elif lista[mitad] > valor:
            return dicotomia(lista[:mitad], valor)
        else:
            return dicotomia(lista[mitad+1:], valor)