"""
Ejercicio 3. Reporte de calificaciones por grupo

Una institución guarda las calificaciones de sus grupos en una lista de listas:

    grupos = [
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ]

Implementa:

    def reporte_grupos(grupos, nota_minima=60):
        pass

La función debe devolver una lista de diccionarios. Cada diccionario contiene:

- "grupo": número del grupo, comenzando en 1.
- "cantidad": cantidad de estudiantes.
- "aprobados": cantidad de notas mayores o iguales que nota_minima.
- "reprobados": cantidad de notas menores que nota_minima.

Ejemplo

    reporte_grupos([
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ])

Resultado esperado:

    [
        {"grupo": 1, "cantidad": 3, "aprobados": 2, "reprobados": 1},
        {"grupo": 2, "cantidad": 0, "aprobados": 0, "reprobados": 0},
        {"grupo": 3, "cantidad": 4, "aprobados": 2, "reprobados": 2}
    ]

Para una lista de grupos vacía:

    reporte_grupos([])   # []

Requisitos

- Utiliza obligatoriamente:

    for numero_grupo, notas in enumerate(grupos, start=1):
        ...

- Reutiliza la función recursiva contar_desde_limite() del ejercicio 2 para
  obtener los aprobados. El archivo ya trae la importación:

    from ejercicio_02.ejercicio_02 import contar_desde_limite

- Calcula los reprobados a partir de la cantidad total y los aprobados.
- No imprimas el reporte: devuélvelo.
- No modifiques las listas recibidas.

Ejecuta este archivo desde la carpeta principal con:
    python -m ejercicio_03.ejercicio_03
"""


def reporte_grupos(grupos, nota_minima=60):
    pass


# ---------------------------------------------------------------------
# Preguntas de análisis (responde debajo de cada pregunta)
# ---------------------------------------------------------------------
# 1. ¿Qué devuelve enumerate() en cada iteración?
#
#
# 2. ¿Qué parte del problema resuelve el ciclo?
#
#
# 3. ¿Qué parte resuelve la función recursiva?
#
#
# 4. ¿Por qué un grupo vacío debe aparecer en el reporte aunque no tenga
#    estudiantes?
#
#


if __name__ == "__main__":
    grupos = [
        [80, 55, 90],
        [],
        [40, 60, 75, 59]
    ]
    print(reporte_grupos(grupos))
    # [{'grupo': 1, 'cantidad': 3, 'aprobados': 2, 'reprobados': 1},
    #  {'grupo': 2, 'cantidad': 0, 'aprobados': 0, 'reprobados': 0},
    #  {'grupo': 3, 'cantidad': 4, 'aprobados': 2, 'reprobados': 2}]

    print(reporte_grupos([]))   # []
