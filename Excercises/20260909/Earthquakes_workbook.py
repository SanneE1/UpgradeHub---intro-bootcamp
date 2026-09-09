"""
Create quick function to get strenght and number of earthquakes

"""

#------------------------------------------------------------------
# Import
# ------------------------------------------------------------------ 
import requests

#------------------------------------------------------------------
# Get the city from user
# ------------------------------------------------------------------
target = float(input("Which magnitude do you want? "))
limit = int(input("What is the maximum number you want to retrieve? "))

#------------------------------------------------------------------
# Get the parameters of the search
#------------------------------------------------------------------

params = {
    "format": "geojson",       
    "minmagnitude": target,    
    "limit": limit,          
    "orderby": "magnitude"
}

respuesta = requests.get(
    "https://earthquake.usgs.gov/fdsnws/event/1/query",
    params=params,
    timeout=10,
)

datos = respuesta.json()

terremotos = datos["features"]

if not terremotos:
    print("No ha habido ninguno tan fuerte. Menos mal.")
    exit()

print()
print(f"Encontrados {len(terremotos)} terremotos de magnitud {target} o mayor en los últimos 30 días")

print(f"{"Magnitude":>4} {"Place":>50} {"Depth":>8}")

for terremoto in terremotos:
    datos_del_terremoto = terremoto["properties"]
    print(f"{datos_del_terremoto["mag"]:>4} {datos_del_terremoto["place"]:>50} {terremoto["geometry"]["coordinates"][2]:>8}")
print()

# 2. Calcula la magnitud media de los que has encontrado.
#    Ve sumando dentro del bucle en una variable `suma` y al final
#    divide entre len(terremotos).
tot_mag = 0
for terremoto in terremotos:
    tot_mag += terremoto["properties"]["mag"]
print(f"The average magnitude of earthquakes over {target} is {tot_mag/len(terremotos)}" )

in_country = 0
for terremoto in terremotos:
    place = terremoto["properties"]["place"]
    if "Indonesia" in place:
        in_country += 1
print(f"Of these earthquakes, {in_country} happened in Indonesia")
