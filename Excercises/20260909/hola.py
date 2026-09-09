"""
hola.py — El archivo .py más pequeño que ya está bien hecho.

Este archivo saluda. Nada más. Pero tiene TODAS las piezas que va a tener
cualquier script del curso, así que merece la pena leerlo despacio.

Uso:
    python3 hola.py            → "Hola, mundo. Bienvenido a Python."
    python3 hola.py Ana        → "Hola, Ana. Bienvenido a Python."
    python3 hola.py "Ana Ruiz" → las comillas mantienen unido el nombre

Requisitos: ninguno. Solo Python.
"""

# ------------------------------------------------------------------------
# IMPORTS
# ------------------------------------------------------------------------
# "import sys" carga el módulo `sys`, que viene incluido con Python y da
# acceso a cosas del sistema. Aquí lo usamos solo para una: sys.argv,
# la lista de palabras que se escribieron en la terminal.
#
# Los imports van SIEMPRE arriba del todo, nunca en medio del archivo.

import sys


# ------------------------------------------------------------------------
# FUNCIONES
# ------------------------------------------------------------------------


def saludar(nombre: str) -> str:
    """
    Devuelve un saludo. Fíjate: DEVUELVE, no imprime.

    El ": str" dice "espero que nombre sea un texto".
    El "-> str" dice "yo te devuelvo un texto".
    Son anotaciones para el que lee; Python no las comprueba y el
    programa funcionaría igual sin ellas.
    """
    # La f delante de las comillas convierte esto en una "f-string":
    # lo que va entre llaves {} se sustituye por el valor de la variable.
    return f"Hola, {nombre}. Bienvenido a Python."

    # ¿POR QUÉ return Y NO print?
    # Porque una función que devuelve texto se puede reutilizar:
    #     mensaje = saludar("Ana")          -> guardarlo
    #     print(saludar("Ana"))             -> imprimirlo
    #     archivo.write(saludar("Ana"))     -> escribirlo en un archivo
    # Si dentro hiciéramos print, solo serviría para lo segundo.


# ------------------------------------------------------------------------
# main()
# ------------------------------------------------------------------------


def main() -> None:
    """
    Punto de entrada del programa: decide qué nombre usar y lo saluda.

    El "-> None" significa "no devuelvo nada", solo tengo el efecto de
    escribir en la pantalla.
    """
    # sys.argv es una LISTA DE TEXTOS con lo que se escribió en la terminal.
    #
    #     python3 hola.py Ana
    #             └──┬──┘ └┬┘
    #        sys.argv[0]  sys.argv[1]
    #
    # sys.argv[0] es siempre el nombre del propio archivo, por eso los
    # datos que nos interesan empiezan en la posición 1.
    #
    # len(sys.argv) cuenta cuántos elementos tiene la lista.
    # Si es mayor que 1, es que el usuario escribió algo detrás del nombre.
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
    else:
        # Si no escribió nada, usamos un valor por defecto en vez de
        # explotar con un error. Un buen script nunca falla por un
        # argumento que falta: o pone un valor por defecto, o avisa.
        nombre = "mundo"

    # Y aquí, por fin, imprimimos. En un solo sitio.
    print(saludar(nombre))


# ------------------------------------------------------------------------
# PUNTO DE ENTRADA — la línea rara, explicada de una vez
# ------------------------------------------------------------------------
#
# Python le pone a cada archivo una variable oculta llamada __name__.
# Su valor depende de CÓMO se esté usando el archivo:
#
#   Caso A — lo lanzas tú:            python3 hola.py
#            __name__ vale "__main__"
#            → la condición de abajo es CIERTA → se ejecuta main() → saluda
#
#   Caso B — otro archivo lo importa: import hola
#            __name__ vale "hola"  (el nombre del archivo)
#            → la condición es FALSA → NO se ejecuta main() → no saluda
#
# ¿Y para qué queremos el caso B? Para poder hacer esto desde otro script:
#
#       import hola
#       print(hola.saludar("clase"))    # uso solo la función que me interesa
#
# ...sin que el programa entero se ponga a ejecutarse sin permiso.
#
# En una frase: estas dos líneas significan
# "ejecuta el programa SOLO si me han lanzado a mí directamente".
#
# Pruébalo tú:  abre una terminal aquí y escribe estas tres líneas
#
#       python3
#       >>> import hola          <- no imprime nada, ¡esa es la gracia!
#       >>> hola.saludar("tú")   <- pero la función está disponible
#
# (para salir del intérprete: exit() )

if __name__ == "__main__":
    main()


# ========================================================================
# EJERCICIOS RÁPIDOS (haz estos antes de pasar a ejercicios.py)
# ========================================================================
#
# 1. Cambia el valor por defecto "mundo" por tu nombre y vuelve a ejecutar
#    `python3 hola.py` sin argumentos.
#
# 2. Quita las dos últimas líneas (el if __name__) y ejecuta el archivo.
#    ¿Qué pasa? ¿Por qué? Vuelve a ponerlas.
#
# 3. Cambia el `return` de saludar() por un `print`. Ejecuta.
#    Verás "None" en pantalla. ¿Sabrías explicar por qué?
#    (pista: si una función no hace return, devuelve None, y main()
#     está imprimiendo lo que devuelve saludar)
