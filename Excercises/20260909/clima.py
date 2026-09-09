"""
clima.py — Pide a una API el tiempo que hace en una ciudad.

Para ejecutarlo, en la terminal:

    pip3 install requests      (solo la primera vez)
    python3 clima.py
"""

# requests es la librería para pedir cosas por internet.
# Es la única que hay que instalar; el resto ya viene con Python.
import requests


# ------------------------------------------------------------------
# 1. Preguntamos la ciudad
# ------------------------------------------------------------------
# input() para el programa y espera a que el usuario escriba algo.
ciudad = input("For which city do you want information? ")


# ------------------------------------------------------------------
# 2. Buscamos sus coordenadas
# ------------------------------------------------------------------
# La API del tiempo no entiende "Madrid": necesita latitud y longitud.
# Así que primero preguntamos a otra API cuáles son.

# Los datos que le mandamos a la API van en un diccionario.
# requests los convierte en la parte de la URL que va después del "?".
parametros = {
    "name": ciudad,      # la ciudad que buscamos
    "count": 1,          # solo queremos el primer resultado
    "language": "es",    # que nos conteste en español
}

# requests.get() hace la llamada y espera la respuesta.
# timeout=10 significa "si en 10 segundos no contesta, ríndete"
# (sin esto, el programa podría quedarse colgado para siempre).
respuesta = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params=parametros,
    timeout=10,
)

# La respuesta llega en formato JSON, que es texto.
# .json() lo convierte en un diccionario de Python normal.
datos = respuesta.json()

# Descomenta esta línea si quieres ver todo lo que devuelve la API:
# print(datos)

# Si la ciudad no existe, la respuesta no trae la clave "results".
if "results" not in datos:
    print(f"No he encontrado ninguna ciudad llamada '{ciudad}'.")
    # exit() termina el programa aquí mismo.
    exit()

# datos["results"] es una lista. Cogemos el primer elemento: el [0].
sitio = datos["results"][0]

latitud = sitio["latitude"]
longitud = sitio["longitude"]

print(f"\nBuscando el tiempo en {sitio['name']}...")


# ------------------------------------------------------------------
# 3. Pedimos el tiempo para esas coordenadas
# ------------------------------------------------------------------
respuesta = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": latitud,
        "longitude": longitud,
        # Los datos que queremos ahora mismo. Estos nombres los decide
        # la API, no nosotros: https://open-meteo.com/en/docs
        "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
    },
    timeout=10,
)

# Aquí la respuesta viene anidada: hay un diccionario dentro de otro.
# Con ["current"] entramos al de dentro, que es el que nos interesa.
tiempo = respuesta.json()["current"]


# ------------------------------------------------------------------
# 4. Lo enseñamos por pantalla
# ------------------------------------------------------------------
# La f delante de las comillas permite meter variables dentro con {}.
print()
print(f"  Temperatura:  {tiempo['temperature_2m']} °C")
print(f"  Humedad:      {tiempo['relative_humidity_2m']} %")
print(f"  Viento:       {tiempo['wind_speed_10m']} km/h")
print()


# ------------------------------------------------------------------
# PARA PROBAR
# ------------------------------------------------------------------
# 1. Ejecútalo con Madrid, con Manila y con una ciudad inventada.
# 2. Descomenta el print(datos) de arriba y mira lo que manda la API.
# 3. Cambia el mensaje del input() por otro.
