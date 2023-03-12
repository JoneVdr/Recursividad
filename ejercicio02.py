#Se llama palíndromo a un texto que es el mismo que su imagen reflejada. Así, por ejemplo, las palabras ’SALAS’, ’oso’, ’26762’ son palíndromos. Es decir, un palíndromo se lee de derecha a izquierda como de izquierda a derecha.
#Con esta definición, ’Salas’ u ’¡oso!’ ya no son palíndromos. En el primero, la letra mayúscula inicial y, en el segundo, el espacio y el signo de exclamación perturban la imagen espejo de la palabra. Igualmente, la frase ’Logré ver gol’ sería un palíndromo si la letra mayúscula al inicio de la frase fuera ’l’, si la letra ’é’ no estuviera acentuada y si se eliminaran los espacios.
#¿Hay frases palíndromas? El problema se complica por los caracteres separadores, como el espacio, los signos de puntuación, etc. Además, una frase bien formada siempre termina con un punto, pero el primer carácter nunca es un punto, lo que responde a la pregunta.
#Vamos a generalizar esta definición ampliándola para simplificar el problema. Se busca un palíndromo entre las cadenas de caracteres alfanuméricos donde todas las letras están en mayúsculas, o todas en minúsculas, como queramos, y donde los caracteres acentuados se han sustituido por sus equivalentes sin acento. ’Logré ver gol’ se convierte en ’LOGREVERGOL’ o ’logrevergol’ y es un palíndromo.
#Entonces reconocer un palíndromo consiste en realizar cuatro tratamientos en el texto que se analiza:
#filtrar el texto para conservar solo caracteres alfanuméricos;
#sustituir los caracteres acentuados por su equivalente sin acento;
#sustituir cada letra por su mayúscula o minúscula;
#verificar que el texto filtrado es igual a su imagen reflejada.
#Aquí podemos ver algunos ejemplos de «frases» que son palíndromos después del filtrado.
#Ejemplos
#Dábale arroz a la zorra el abad
#Logré ver gol
#Salas
#1754571
#10000000000000000001
#Oso
#Ejercicio resuelto 6: reconocer un palíndromo
#Hacer un algoritmo que reconozca un palíndromo.
#Puede encontrar una solución estudiada de este ejercicio en los complementos disponibles para descargar desde la página Información.

#Solución
import unicode
def polindromo(frase):
    frase = input("Introduce una frase: ")
    frase = frase.lower()
    frase = unicode(frase)

    if frase == frase[::-1]:
        return "Es un polindromo"
    else:
        return "No es un polindromo"
        return frase

print(polindromo(frase))
