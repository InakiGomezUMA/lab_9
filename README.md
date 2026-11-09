# Laboratorio individual: Recursión

Duracion: 3 horas. 

Entrega: enlace al repositorio individual en GitHub.

Ejercicios principales: 1, 2, 3 y 4. Retos de ampliacion: 5 y 6.

En este laboratorio vas a implementar funciones recursivas, compararlas con versiones iterativas y combinarlas para construir reportes. Varios ejercicios reutilizan funciones de ejercicios anteriores, así que resuélvelos en orden.

## Inicio

1. En GitHub, usa **Use this template > Create a new repository**.
2. Crea tu repositorio individual y clona ESE repositorio, no el original.
3. Comprueba con `git remote -v` que origin corresponde a tu repositorio.
4. Abre la carpeta del repositorio en VS Code.

## Estructura del repositorio

```text
Laboratorio_9/
├── README.md
├── DATOS_ESTUDIANTE.md
├── .gitignore
├── ejercicio_01/
│   └── ejercicio_01.py
├── ejercicio_02/
│   └── ejercicio_02.py
├── ejercicio_03/
│   └── ejercicio_03.py
├── ejercicio_04/
│   └── ejercicio_04.py
├── ejercicio_05/
│   └── ejercicio_05.py
└── ejercicio_06/
    └── ejercicio_06.py
```

Cada archivo `.py` trae la función que debes completar, las preguntas de análisis como comentarios y algunos ejemplos para probar tu solución.

## ¿Cómo trabajar?

1. Completa cada función en lugar de `pass`.
2. Responde las preguntas de análisis **en los comentarios** del mismo archivo, debajo de cada pregunta.
3. No borres ni cambies el nombre de las funciones: los ejercicios 3 y 6 las importan.
4. No modifiques la línea `if __name__ == "__main__":`. Gracias a ella, los ejemplos de un ejercicio no se ejecutan cuando otro ejercicio importa sus funciones.

## Ejecutar desde la raiz del repositorio

```bash
python ejercicio_1/main.py
```

Cambia el numero para ejecutar los demas. Si tu sistema utiliza python3,
sustituye python por python3.

> **Importante:** los ejercicios 3 y 6 importan funciones de otras carpetas. 

## Entrega

Sube tu trabajo a tu repositorio antes del cierre del laboratorio. Cada archivo debe tener la función implementada y las preguntas de análisis respondidas.

El **ejercicio 6 es un reto**: resuélvelo si terminas los ejercicios 1 al 5.

## Guardar y subir cada ejercicio

La plantilla esta pensada para la rama main. Compruebala con `git branch --show-current`.

```bash
git status
git add ejercicio_1/main.py
git commit -m "Completado ejercicio 1"
git push origin main

```
Adapta la ruta y el mensaje a cada ejercicio. Si no terminas un ejercicio,
guarda tambien tu avance con un mensaje que indique que esta incompleto.

## Registro final
- Ejercicios completados:
- Retos completados:
- Ejercicios incompletos y que falta:
- Dificultad encontrada y como la resolvi:

Antes de entregar, comprueba en GitHub que aparecen los archivos actualizados
y los commits. Entrega el enlace al repositorio; debe ser accesible a la profesora.

