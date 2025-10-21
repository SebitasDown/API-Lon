import requests;

ciudades = []

# Función para obtener coordenadas usando la API de Open-Meteo
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
# Bucle principal para solicitar ciudades y obtener coordenadas
while True:
    ciudad = input("🌍 Ingrese el nombre de la ciudad: ")

    lat, lon, nombre = obtener_coordenadas(ciudad)

    # Se verifica que se hayan obtenido latitud y longitud
    if lat and lon:
        ciudades.append({"Ciudad":nombre, "Latitud": lat, "Longitud": lon}) 
        seleccion = input("¿Deseas intentar con otra ciudad? (si/no): ").strip().lower()
        if seleccion == "no":
            print("Coordenadas registradas:")
            for c in ciudades:
                print(c)
            print("Cerrando programa")
            break
    else:
        print("Intenta con otra ciudad.")
        continue
            
    # constructor final
    print("Coordenadas registradas:")
    for c in ciudades:
        print(c)