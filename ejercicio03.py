#El enunciado del problema es el siguiente:
#Consideramos un conjunto de n fichas de colores. Cada ficha es de un solo color. Algunas son rojas, otras verdes y otras son azules. Inicialmente, las fichas no están alineadas en orden. El problema consiste en obtener una organización de las fichas en tres series de fichas del mismo color: primero fichas rojas, luego fichas verdes y después fichas azules. Esta organización debe obtenerse mediante intercambios sucesivos, pero el color de cada ficha solo se comprueba una vez.
#Hacer un algoritmo que produzca esta ordenación para un número cualquiera de fichas.
#Cada color está representado por un número cualquiera de fichas y, en particular, puede faltar un color del conjunto. El dibujo de la figura que aparece a continuación representa un conjunto de 17 fichas en las situaciones de antes y después de la ejecución del algoritmo que se ha de definir.
#El conjunto por ordenar está formado por 17 fichas de las que 7 son rojas, 6 son azules y 4 son verdes. El resultado de ordenarlas reúne las 7 fichas rojas, seguidas de las 4 fichas verdes y de las 6 fichas azules. Este orden es el RVB de tres colores y no el orden decreciente de los efectivos de tres colores. Es decir, se han ordenado los colores de las fichas en el orden R, luego V y después B, y no por los números de fichas en cada subconjunto de colores.
#Solución
#Una norma importante que debemos respetar es « … el color de cada ficha solo se comprueba una vez.» Esta norma es la que crea la dificultad del problema. Es fundamental hacer un análisis cuidadoso y construir una solución que permita una clasificación correcta, incluso cuando hay colores no representados. Como es habitual, el análisis de la solución estará condicionado por la descripción precisa de un estado intermedio.
#Consideramos un estado intermedio, donde se ha realizado parte de la clasificación. Entonces algunas fichas todavía no se han colocado en su lugar. La idea creativa para este problema se la debemos a Dijkstra. Consiste en repartir las fichas en cuatro subconjuntos: rojas, verdes, fichas no ordenadas y azules, en este orden. Esta situación genérica se representa mediante el diseño de la figura que aparece a continuación.
#La hipótesis es que i fichas rojas, j-i fichas verdes y n-k fichas azules están en su lugar, mientras que todavía no hemos accedido a k-j fichas. Así, i representa el número de fichas rojas colocadas; j representa el número de fichas rojas y verdes colocadas; k representa el número de fichas rojas y verdes colocadas sumadas con las que todavía no hemos comprobado. Los índices de los lugares que ocupan pueden verse en el dibujo. Muestra que las fichas rojas ocupan las posiciones de índices de 1 a i; las verdes ocupan las posiciones de índices de i + 1 a j; las fichas que no se han colocado ocupan las posiciones de índices de j + 1 a k y, por último, las fichas azules ocupan las posiciones con los índices de k + 1 a n.
#Puede encontrar una solución de este ejercicio en los complementos asociados a este libro y disponibles para descargar desde la página Información. Los dibujos de esta solución están en color y así son más fáciles de comprender.

#Solución
def color(rojo, azul, verdes, posicion):
    if posicion <= rojo:
        return 'rojo'
    elif posicion <= rojo + verdes:
        return 'verde'
    elif posicion <= rojo + verdes + azul:
        return 'azul'
    else:
        return 'no ordenado'