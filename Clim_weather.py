# Lista de Ciudades
ciudades = ["Bogotá", "Medellín", "Cali"]
# Donde se guardaran los diccionarios
coordenadas_ciudades = []

# Funcion principal donde se obtiene la longitud y la latitud
def obtener_coordenadas ():
    while True:
        # Imprime las ciudades
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
        
        # Seleccion para cerrar bucle
        seleccion = input("¿Deseas ponerle lon y lat a otra ciudad? (si/no): ").strip().lower()
        if seleccion == "no":
            print("Finalizado")
            break

obtener_coordenadas();

print("Coordenadas registradas")
for c in coordenadas_ciudades:
    print(c)


