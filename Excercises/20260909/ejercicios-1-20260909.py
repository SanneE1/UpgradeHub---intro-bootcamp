"""
ejercicios.py — Lección 1. Rellena los huecos marcados con TODO.

Cómo trabajar con este archivo:

    1. Ejecútalo tal cual:   python3 ejercicios.py
       Verás que los tests fallan. Es normal, todavía no has escrito nada.
    2. Ve resolviendo los ejercicios de arriba abajo.
    3. Vuelve a ejecutar después de cada uno hasta que salga "CORRECTO".
    4. Solo cuando lo hayas intentado, mira soluciones.py

No hay que tocar nada por debajo de la línea de "COMPROBACIONES".
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
    # TODO: sustituye la línea de abajo por tu return con una f-string
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
    fahrenheit = celsius * 9 / 5 + 32

    return fahrenheit


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
    # TODO: usa if / elif / else
    if grados > 30:
        answer = "hace calor"
    elif grados >= 15:
        answer = "se está bien"
    else:
        answer = "hace frío"

    return answer

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
    if len(argumentos) > 1:
        nombre = argumentos[1]
    else:
        nombre = "sin argumentos"

    return nombre


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


def main() -> None:
    """Ejecuta el programa principal."""
    nombre = primer_argumento(sys.argv)

    if nombre == "sin argumentos":
        print("Uso: python3 ejercicios.py <nombre>")
        return

    import hola

    print(hola.saludar(nombre))
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
