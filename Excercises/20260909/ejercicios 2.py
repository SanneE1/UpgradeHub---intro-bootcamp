"""
ejercicios.py — Lección 1. RESUELTO.

Ejecutar:
    python3 ejercicios.py          -> comprueba los ejercicios
    python3 ejercicios.py Ana      -> ejecuta main() con un nombre
"""

import sys


# ========================================================================
# EJERCICIO 1 — Tu primera función
# ========================================================================
# Escribe una función que reciba un nombre y devuelva una despedida.
#
#     despedir("Ana")  ->  "Adiós, Ana. Hasta la próxima."
#
# Recuerda: DEVOLVER (return), no imprimir (print).


def despedir(nombre: str) -> str:
    """Devuelve una despedida para ese nombre."""
    # La f delante de las comillas permite meter la variable entre {}.
    return f"Adiós, {nombre}. Hasta la próxima."


# ========================================================================
# EJERCICIO 2 — Un cálculo sencillo
# ========================================================================
# Escribe una función que convierta grados Celsius a Fahrenheit.
# La fórmula es:   fahrenheit = celsius * 9 / 5 + 32
#
#     a_fahrenheit(0)    ->  32.0
#     a_fahrenheit(100)  ->  212.0


def a_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit."""
    # Primero se hacen la multiplicación y la división, después la suma,
    # así que no hacen falta paréntesis. En Python 3, 9 / 5 da 1.8
    # (con decimales); si usaras // daría 1 y el resultado sería erróneo.
    return celsius * 9 / 5 + 32


# ========================================================================
# EJERCICIO 3 — Decidir con if
# ========================================================================
# Escribe una función que describa una temperatura:
#
#     mas de 30      ->  "hace calor"
#     entre 15 y 30  ->  "se está bien"
#     menos de 15    ->  "hace frío"
#
# Ojo con los bordes: 30 exactos es "se está bien", 15 exactos también.


def describir_temperatura(grados: float) -> str:
    """Devuelve una frase describiendo esa temperatura."""
    # Los if/elif se miran EN ORDEN y se para en el primero que se cumple.
    # Por eso el segundo no necesita comprobar "grados <= 30": si hemos
    # llegado ahí es que el primero era falso, o sea que ya es <= 30.
    if grados > 30:
        return "hace calor"
    elif grados >= 15:
        return "se está bien"
    else:
        return "hace frío"


# ========================================================================
# EJERCICIO 4 — Trabajar con la lista de argumentos
# ========================================================================
# Escribe una función que reciba la lista sys.argv (entera, con el nombre
# del archivo dentro) y devuelva SOLO el primer argumento del usuario.
# Si el usuario no escribió ninguno, devuelve el texto "sin argumentos".
#
#     primer_argumento(["hola.py"])              ->  "sin argumentos"
#     primer_argumento(["hola.py", "Ana"])       ->  "Ana"
#     primer_argumento(["hola.py", "Ana", "Bea"]) ->  "Ana"
#
# Pista: len(lista) te dice cuántos elementos tiene.


def primer_argumento(argumentos: list) -> str:
    """Devuelve el primer argumento del usuario, o 'sin argumentos'."""
    # La posición 0 es el nombre del archivo, así que lo que escribió
    # el usuario empieza en la 1. Hay que comprobar la longitud ANTES
    # de leer argumentos[1]: si la lista es corta, salta IndexError.
    if len(argumentos) > 1:
        return argumentos[1]
    return "sin argumentos"


# ========================================================================
# EJERCICIO 5 — Juntarlo todo en un main()
# ========================================================================
# Completa main() para que el script:
#
#   1. Coja el primer argumento con la función del ejercicio 4.
#   2. Si vale "sin argumentos", imprima:  Uso: python3 ejercicios.py <nombre>
#      y termine (con return).
#   3. Si hay nombre, imprima el saludo Y la despedida, uno por línea.
#
# Pruébalo con:   python3 ejercicios.py Ana


def saludar(nombre: str) -> str:
    """Devuelve un saludo. Hace falta para el paso 3 del ejercicio 5."""
    return f"Hola, {nombre}. Bienvenido a Python."


def main() -> None:
    # 1. Cogemos el primer argumento de lo que se escribió en la terminal.
    nombre = primer_argumento(sys.argv)

    # 2. Si no había ninguno, explicamos cómo se usa y salimos.
    #    `return` dentro de main() termina la función, y con ella el programa.
    if nombre == "sin argumentos":
        print("Uso: python3 ejercicios.py <nombre>")
        return

    # 3. Y si sí había, saludamos y nos despedimos.
    print(saludar(nombre))
    print(despedir(nombre))


# ========================================================================
# COMPROBACIONES — no toques nada de aquí para abajo
# ========================================================================


def comprobar(descripcion: str, obtenido, esperado) -> bool:
    """Compara lo obtenido con lo esperado e imprime el resultado."""
    if obtenido == esperado:
        print(f"  CORRECTO   {descripcion}")
        return True
    print(f"  FALLA      {descripcion}")
    print(f"             esperaba: {esperado!r}")
    print(f"             obtuve:   {obtenido!r}")
    return False


def pasar_tests() -> None:
    print("\n  Resultado de los ejercicios")
    print("  " + "-" * 55)

    resultados = [
        comprobar("1. despedir('Ana')",
                  despedir("Ana"), "Adiós, Ana. Hasta la próxima."),
        comprobar("2. a_fahrenheit(0)", a_fahrenheit(0), 32.0),
        comprobar("2. a_fahrenheit(100)", a_fahrenheit(100), 212.0),
        comprobar("3. describir_temperatura(35)",
                  describir_temperatura(35), "hace calor"),
        comprobar("3. describir_temperatura(20)",
                  describir_temperatura(20), "se está bien"),
        comprobar("3. describir_temperatura(5)",
                  describir_temperatura(5), "hace frío"),
        comprobar("4. primer_argumento(['x.py'])",
                  primer_argumento(["x.py"]), "sin argumentos"),
        comprobar("4. primer_argumento(['x.py', 'Ana'])",
                  primer_argumento(["x.py", "Ana"]), "Ana"),
    ]

    print("  " + "-" * 55)
    print(f"  {sum(resultados)} de {len(resultados)} correctos\n")


if __name__ == "__main__":
    pasar_tests()
    print("  --- salida de tu main() ---\n")
    main()
    print()
