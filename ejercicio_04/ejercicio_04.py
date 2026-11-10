"""
Ejercicio 4. Buscar un código en un catálogo ordenado

Un catálogo contiene códigos numéricos ordenados de menor a mayor. Implementa
una búsqueda binaria recursiva para localizar un código.

    def buscar_codigo(codigos, objetivo, izquierda, derecha):
        pass

La función devuelve el índice del código si se encuentra, o -1 si no se
encuentra. Si hay códigos repetidos, puedes devolver el índice de cualquiera de
sus apariciones.

Ejemplos

    codigos = [101, 205, 310, 415, 520, 630, 740]

    buscar_codigo(codigos, 520, 0, len(codigos) - 1)   # 4
    buscar_codigo(codigos, 300, 0, len(codigos) - 1)   # -1
    buscar_codigo([], 300, 0, -1)                      # -1
    buscar_codigo([205], 205, 0, 0)                    # 0

Restricciones

- La solución debe ser recursiva.
- No utilices ciclos ni cortes.
- No busques con objetivo in codigos ni con .index().
- No ordenes la lista dentro de la función: se recibe ordenada.
- En cada llamada, continúa únicamente en la región que todavía pueda contener
  el objetivo.
"""


def buscar_codigo(codigos, objetivo, izquierda, derecha):
    """Busca un código de forma binaria y recursiva. Devuelve el índice si se encuentra, o -1 en caso contrario."""
    
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if codigos[medio] == objetivo:
        return medio
    
    elif objetivo < codigos[medio]:
        return buscar_codigo(codigos, objetivo, izquierda, medio - 1)
    
    else:
        return buscar_codigo(codigos, objetivo, medio + 1, derecha)


if __name__ == "__main__":
    codigos = [101, 205, 310, 415, 520, 630, 740]

    print(buscar_codigo(codigos, 520, 0, len(codigos) - 1))   # 4
    print(buscar_codigo(codigos, 300, 0, len(codigos) - 1))   # -1
    print(buscar_codigo([], 300, 0, -1))                       # -1
    print(buscar_codigo([205], 205, 0, 0))                    # 0

# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuáles son las dos situaciones en las que termina la búsqueda?
#
#  Se encuentra el código objetivo.
#
# 2. ¿Por qué no debes incluir nuevamente la posición central en el
#    siguiente intervalo?
#
#  Porque ya hemos verificado que el código no está en esa posición.
#
# 3. Completa la traza buscando 300 en codigos. Si una llamada no llega a
#    calcular el medio, escribe "—".
#
#    Llamada | Izquierda | Derecha | Medio | Decisión
#    --------|-----------|---------|-------|---------
#       1    |     0      |     6   |   3   |  Izquierda
#       2    |     0      |     2   |   1   |  Derecha
#       3    |     2      |     2   |   2   |  Izquierda
#       4    |     2      |     1   |   —   |  Termina
#
# 4. ¿Qué diferencia hay entre el progreso de esta función y el de contar_desde_limite()?
#
#  La función buscar_codigo reduce el intervalo de búsqueda a la mitad en cada llamada, mientras que contar_desde_limite() incrementa el contador en cada llamada.
#