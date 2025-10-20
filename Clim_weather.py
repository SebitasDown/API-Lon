ciudades = ["Bogotá", "Medellín", "Cali"]
coordenadas_ciudades = []

def obtener_coordenadas ():
    while True:
        for ciudad in ciudades:
            print("-", ciudad)


        c = input("¿Que ciudad deseas agregarle lat y lon?: ").strip()
        if c in ciudades:
            print("Ciudad seleccionada ", c)
            try:
                lat = input("Ingresa la latitud: ")
                lon = input("Ingresa la longitud: ")
                coordenadas_ciudades.append({"nombre": c, "lat": lat, "lon": lon})
                print(f"coordenadas agregadas para {c}")
            except ValueError:
                print("Valores no validos. Ingresa numeros validos")
        else:
            print("Ciudad no encontrada")        

        seleccion = input("¿Deseas ponerle lon y lat a otra ciudad? (si/no): ").strip().lower()
        if seleccion == "no":
            print("Finalizado")
            break

obtener_coordenadas();

print("Coordenadas registradas")
for c in coordenadas_ciudades:
    print(c)



 

 






ciudades_info = [
    {"nombre": "Bogotá", "lat": 4.71, "lon": -74.07},
    {"nombre": "Medellín", "lat": 6.25, "lon": -75.56},
    {"nombre": "Cali", "lat": 3.45, "lon": -76.54},
    {"nombre": "Barranquilla", "lat": 10.96, "lon": -74.79},
    {"nombre": "Cartagena", "lat": 10.40, "lon": -75.51},
    {"nombre": "Bucaramanga", "lat": 7.12, "lon": -73.10},
    {"nombre": "Cúcuta", "lat": 7.90, "lon": -72.50},
    {"nombre": "Pereira", "lat": 4.81, "lon": -75.69}
]

def obtener_coordenada():
    for ciudad in ciudades_info:
        print(f"Ciudad: {ciudad['nombre']}, Latitud: {ciudad['lat']}, Longitud: {ciudad['lon']}")



