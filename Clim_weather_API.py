import requests;

ciudades = []


def obtener_coordenadas(ciudad):
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    parametros = {"name": ciudad, "count": 1, "language": "es"}

    resp = requests.get(geo_url, params=parametros)
    data = resp.json()
    
    if resp.status_code == 200  and data.get("results"):
        datos = resp.json()["results"][0]
        return datos["latitude"], datos["longitude"], datos["name"]
    else:
        print("No se encontro la ciudad")
        return None, None, None

while True:
    ciudad = input("🌍 Ingrese el nombre de la ciudad: ")

    lat, lon, nombre = obtener_coordenadas(ciudad)


    if lat and lon:
        ciudades.append({"Ciudad":nombre, "Latitud": lat, "Longitud": lon})