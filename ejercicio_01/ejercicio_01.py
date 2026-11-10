"""
Ejercicio 1. Potencia recursiva

Implementa una función que calcule una potencia mediante multiplicaciones y
llamadas recursivas. Recibe una base numérica y un exponente entero no
negativo.

    def potencia(base, exponente):
        pass

En este ejercicio, cualquier base elevada a cero devuelve 1, incluido
potencia(0, 0).

Ejemplos

    potencia(2, 4)    # 16
    potencia(5, 0)    # 1
    potencia(-2, 3)   # -8
    potencia(0, 5)    # 0

Restricciones

- No utilices ciclos.
- No utilices  ni pow().
- La solución debe ser recursiva.
"""

from email.mime import base


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

if __name__ == "__main__":
    print(potencia(2, 4))    # 16
    print(potencia(5, 0))    # 1
    print(potencia(-2, 3))   # -8
    print(potencia(0, 5))    # 0

# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Cuál es el caso base?
#
# exponente == 0, que devuelve 1
#
# 2. ¿Qué argumento cambia en cada llamada?
#
# exponente , (exponente - 1) en cada llamada recursiva
#
# 3. ¿Qué operación queda pendiente mientras se resuelve la llamada recursiva?
#
# La multiplicación de la base por el resultado de la llamada recursiva.
#
# 4. Escribe las llamadas y los retornos de potencia(3, 3).
#
# Fase de llamadas (Pila descendente):
#potencia(3, 3) llama a 3 * potencia(3, 2)
#potencia(3, 2) llama a 3 * potencia(3, 1)
#potencia(3, 1) llama a 3 * potencia(3, 0)
#potencia(3, 0) cumple el caso base y retorna 1
#potencia(3, 0) retorna 1
#potencia(3, 1) resuelve 3 * 1 y retorna 3
#potencia(3, 2) resuelve 3 * 3 y retorna 9
#potencia(3, 3) resuelve 3 * 9 y retorna 27
#