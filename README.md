# Mini juegos en Python

Colección de cuatro juegos de consola desarrollados en Python como proyecto de práctica para construir lógica de programación sólida, con código organizado y fácil de ejecutar.

## Vista general

Cada juego es independiente y se ejecuta por separado. No requiere librerías externas, solo la biblioteca estándar de Python.

| Juego | Qué demuestra |
|---|---|
| **Adivina el número** | Bucles, condicionales, validación de entrada y manejo de errores con `try` / `except` |
| **Piedra, papel o tijera** | Diccionarios para reglas del juego, control de flujo y manejo de marcador |
| **Ahorcado** | Conjuntos (`set`), manipulación de cadenas y control de estado del juego |
| **Dados a 50** | Lógica por turnos, números aleatorios y condiciones de victoria |

## Habilidades aplicadas

- Estructuras de control: `if`, `elif`, `else`, `while` y `break`
- Validación de datos ingresados por el usuario
- Manejo de errores con `try` / `except`
- Uso de tipos de datos: enteros, cadenas, listas, diccionarios y conjuntos
- Generación de valores aleatorios con el módulo `random`
- Código organizado en funciones con bloque `if __name__ == "__main__":`

## Requisitos

- Python 3.8 o superior

## Cómo ejecutarlos

Los juegos están en la carpeta `Mini juegos`. Desde la raíz del repositorio, ejecuta el que quieras:

```bash
python "Mini juegos/adivina el numero.py"
python "Mini juegos/piedra_papel_tijera.py"
python "Mini juegos/ahorcado.py"
python "Mini juegos/dados_a_50.py"
```

Las comillas son necesarias porque el nombre de la carpeta y del primer archivo tienen espacios.

## Próximas mejoras

- Guardar el récord de cada juego en un archivo.
- Agregar un menú principal para elegir el juego.
- Añadir pruebas automáticas con `unittest`.

## Autor

Proyecto personal de aprendizaje en Python.
