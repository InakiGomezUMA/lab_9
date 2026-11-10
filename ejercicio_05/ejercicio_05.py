"""
Ejercicio 5. Extraer valores de una estructura anidada

Un sistema recibe mediciones agrupadas en listas que pueden contener otras
listas, con distintos niveles de profundidad.

    def extraer_valores(datos):
        pass

La función devuelve una nueva lista plana con todos los números, en el orden en
que aparecen de izquierda a derecha. Las entradas contienen únicamente números
y listas, y no tienen referencias cíclicas.

Ejemplos

    extraer_valores([10, [20, 30], 40])     # [10, 20, 30, 40]
    extraer_valores([1, [2, [], [3]], 4])   # [1, 2, 3, 4]
    extraer_valores([[], [[], []]])         # []
    extraer_valores([])                     # []

Requisitos

- Utiliza un ciclo para recorrer los elementos del nivel actual.
- Si encuentras un número, incorpóralo al resultado.
- Si encuentras una lista, procésala mediante una llamada recursiva.
- Puedes utilizar append() y extend().
- No utilices cortes.
- No modifiques la estructura original.
- No dejes sublistas dentro del resultado.
"""

def extraer_valores(datos):
    """Extrae todos los números de una estructura anidada de listas aplanándolos en una sola lista."""
    resultado = []
    
    for elemento in datos:
        # Si el elemento es una lista, realizamos una llamada recursiva y extendemos el resultado
        if isinstance(elemento, list):
            resultado.extend(extraer_valores(elemento))
        # Si es un número (o cualquier otro valor no lista), lo agregamos directamente
        else:
            resultado.append(elemento)
            
    return resultado


if __name__ == "__main__":
    print(extraer_valores([10, [20, 30], 40]))     # [10, 20, 30, 40]
    print(extraer_valores([1, [2, [], [3]], 4]))   # [1, 2, 3, 4]
    print(extraer_valores([[], [[], []]]))         # []
    print(extraer_valores([]))                     # []

# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve la función cuando recibe una lista vacía?
#
#Devuelve una lista vacía ([]). Al recibir una lista vacía, el ciclo for no llega a ejecutarse, por lo que la función retorna directamente la variable resultado inicializada al principio, la cual está vacía.
#
# 2. ¿Qué diferencia hay entre incorporar un número e incorporar el resultado de una llamada recursiva?
#
#Incorporar un número: Se realiza utilizando el método .append porque el número es un valor único que se agrega directamente como un nuevo elemento al final de la lista del nivel actual.
#
#Incorporar el resultado de una llamada recursiva: Se realiza utilizando el método .extend porque la llamada recursiva devuelve otra lista con valores ya aplanados. Con extend, se incorporan todos los elementos individuales de esa sublista de golpe, evitando que queden listas anidadas dentro del resultado.
#
# 3. Dibuja únicamente las llamadas a extraer_valores() para[1, [2, [], [1]], 4]. ¿Cuántas llamadas se realizan, incluyendo las de listas vacías?
#
#extraer_valores([1, [2, [], [1]], 4]) (Llamada principal)
#
#Contiene la sublista [2, [], [1]], lo que genera la llamada:
#
#Dentro de esta, encuentra la sublista vacía [], lo que genera la llamada:
#
#Y también encuentra la sublista [1], lo que genera la llamada:
#
extraer_valores([1])
#
# 4. ¿Por qué cada llamada necesita su propia lista de resultados?
#
#Porque cada nivel de anidamiento (cada sublista) representa un subproblema independiente.
#