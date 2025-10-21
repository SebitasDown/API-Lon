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

def obtener_clima(lat, lon):
    clima_url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude" : lat,
        "longitude" : lon,
        "current_weather": True
    }

    resp = requests.get(clima_url, params=parametros)

    if resp.status_code == 200:
        return resp.json().get("current_weather", None)
    else:
        print("Error al obtener el clima")
        return None    


# Bucle principal para solicitar ciudades y obtener coordenadas
while True:
    ciudad = input("🌍 Ingrese el nombre de la ciudad: ")

    lat, lon, nombre = obtener_coordenadas(ciudad)

    if lat and lon:
        clima = obtener_clima(lat,lon)
        if clima:
            temperatura = clima["temperature"]    
            codigo = clima["weathercode"]


            codigos = {
                0: "Despejado ☀️",
                1: "Mayormente despejado 🌤️",
                2: "Parcialmente nublado ⛅",
                3: "Nublado ☁️",
                45: "Niebla 🌫️",
                48: "Niebla con escarcha 🌫️❄️",
                51: "Llovizna ligera 🌦️",
                61: "Lluvia 🌧️",
                71: "Nieve ❄️",
                95: "Tormenta eléctrica ⛈️"
            }
            descripcion = codigos.get(codigo, "Condicion desconocida")
    # Se verifica que se hayan obtenido latitud y longitud
    if lat and lon:
        ciudades.append({"Ciudad":nombre, "Latitud": lat, "Longitud": lon,"Temperatura": temperatura, "Clima": descripcion}) 
        print("Coordenadas registradas:")
        # Reorganizar el constructor
        for c in ciudades:
            print(c)
        seleccion = input("¿Deseas intentar con otra ciudad? (si/no): ").strip().lower()
        if seleccion == "no":
            print("Cerrando programa")
            break
    else:
        print("Intenta con otra ciudad.")
        continue
            
    # constructor final
print("Ranking:")
ranking = sorted (ciudades, key=lambda c: c["Temperatura"], reverse= True)
for i, c in enumerate(ranking, start=1):
    print(f"{i}. {c['Ciudad']}: {c['Temperatura']}°C - {c['Clima']}")