"""
ejercicio.py — Ahora te toca a ti.

OBJETIVO
--------
Escribir un programa que pregunte una magnitud mínima y liste los
terremotos que ha registrado el USGS (el servicio geológico de Estados
Unidos) en los últimos 30 días.

Son datos sismológicos reales y actualizados. La API es gratis y no
necesita registro:

    https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=6&limit=10&orderby=magnitude

Si abres esa dirección en el navegador verás lo que devuelve. Es un
diccionario grande, pero solo nos interesa una parte:

    {
      "type": "FeatureCollection",
      "metadata": {...},
      "features": [                          <-- la lista de terremotos
         {"properties": {"mag": 7.8,
                         "place": "64 km NNW of Ende, Indonesia",
                         "time": 1786744701505}},
         {"properties": {"mag": 6.9,
                         "place": "9 km WNW of Pematangsiantar, Indonesia"}},
         ...
      ]
    }


ASÍ TIENE QUE FUNCIONAR
-----------------------
    $ python3 ejercicio.py
    ¿Magnitud mínima? 6

    Encontrados 10 terremotos de magnitud 6.0 o mayor
    en los últimos 30 días:

      7.8   64 km NNW of Ende, Indonesia
      6.9   9 km WNW of Pematangsiantar, Indonesia
      6.7   37 km NE of Tambo, Peru
      6.3   84 km SSW of Nikolski, Alaska
      ...


LO NUEVO RESPECTO A clima.py
----------------------------
Aquí la API no devuelve UN resultado, sino una LISTA de resultados.
Para enseñarlos todos hace falta un bucle `for`. Es el único concepto
nuevo del ejercicio.


PASOS
-----
Sigue los TODO de abajo, en orden. Ejecuta el programa después de
cada paso para ir viendo si funciona.

Ten abierto clima.py de la otra carpeta: la estructura es la misma
(preguntar, llamar a la API, enseñar el resultado).
"""

# TODO 1: importa la librería requests
#         (una sola línea, igual que en clima.py)


# ------------------------------------------------------------------
# TODO 2: pregunta la magnitud mínima y guárdala en `magnitud`.
#
#         OJO: input() siempre devuelve TEXTO, aunque escriban "6".
#         Para que la API lo entienda como número, conviértelo:
#             magnitud = float(input("¿Magnitud mínima? "))
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 3: llama a la API.
#
#         La dirección es:
#             https://earthquake.usgs.gov/fdsnws/event/1/query
#
#         y hay que mandarle cuatro datos:
#             format        ->  "geojson"       (el formato de respuesta)
#             minmagnitude  ->  magnitud        (lo que pidió el usuario)
#             limit         ->  10              (máximo 10 resultados)
#             orderby       ->  "magnitude"     (del más fuerte al más flojo)
#
#         Copia la forma de clima.py:
#
#             respuesta = requests.get(
#                 "...la dirección...",
#                 params={...los cuatro datos...},
#                 timeout=10,
#             )
#             datos = respuesta.json()
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 4: saca la lista de terremotos.
#
#         Está dentro de datos, en la clave "features":
#             terremotos = datos["features"]
#
#         Añade esta línea para comprobar que la tienes:
#             print(len(terremotos))
#         (bórrala cuando ya funcione; len() cuenta los elementos)
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 5: si no hay ninguno, dilo y termina.
#
#         Una lista vacía se considera "falsa" en Python, así que:
#
#             if not terremotos:
#                 print("No ha habido ninguno tan fuerte. Menos mal.")
#                 exit()
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 6: imprime cuántos has encontrado.
#
#         Algo como:
#             Encontrados 10 terremotos de magnitud 6.0 o mayor
#             en los últimos 30 días:
#
#         Usa una f-string con {len(terremotos)} y {magnitud}.
# ------------------------------------------------------------------


# ------------------------------------------------------------------
# TODO 7: recórrelos con un bucle e imprime cada uno.
#
#         Esto es lo nuevo del ejercicio. Un `for` va sacando los
#         elementos de la lista de uno en uno:
#
#             for terremoto in terremotos:
#                 datos_del_terremoto = terremoto["properties"]
#                 print(datos_del_terremoto["mag"], datos_del_terremoto["place"])
#
#         Fíjate en la sangría: lo que va DENTRO del for lleva 4
#         espacios por delante. Python usa los espacios para saber
#         qué está dentro y qué está fuera del bucle.
# ------------------------------------------------------------------


# ==================================================================
# SI TE SOBRA TIEMPO
# ==================================================================
# 1. Alinea la tabla para que se lea mejor:
#        print(f"  {mag:>4}   {place}")
#    ({mag:>4} coloca el número a la derecha ocupando 4 huecos)
#
# 2. Calcula la magnitud media de los que has encontrado.
#    Ve sumando dentro del bucle en una variable `suma` y al final
#    divide entre len(terremotos).
#
# 3. Cuenta cuántos han sido en un país concreto. El país está al
#    final del texto de "place", así que sirve:
#        if "Indonesia" in place:
#
# 4. Sube el límite a 50 (limit) y prueba con magnitud 4.5.
#
# 5. Añade la profundidad. Está en otro sitio del diccionario:
#        terremoto["geometry"]["coordinates"][2]     (en kilómetros)
#    Es un buen ejercicio de bucear en un JSON anidado.
