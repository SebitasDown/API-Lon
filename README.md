# 🌍 Clim Weather - Sistema de Gestión de Coordenadas

Colección de scripts en Python para gestionar coordenadas geográficas de ciudades, tanto manualmente como mediante integración con API de geocodificación.

## 📋 Descripción

Proyecto educativo que demuestra dos enfoques para trabajar con coordenadas geográficas:
1. **Manual**: Registro manual de latitud y longitud para ciudades predefinidas
2. **Automático**: Obtención automática de coordenadas mediante API de Open-Meteo

## 🛠️ Tecnologías

- **Python 3.x** 🐍
- **requests** (para versión API)
- **Open-Meteo Geocoding API**

## 📂 Estructura del Proyecto

    📦 clim-weather/
    ├── 📄 Clim_weather.py (Versión manual)
    └── 📄 Clim_weather_API.py (Versión con API)

## ⚙️ Instalación

### 1️⃣ Para versión manual

    python Clim_weather.py

### 2️⃣ Para versión con API

    pip install requests
    python Clim_weather_API.py

## 📝 Scripts Incluidos

### 📍 Clim_weather.py - Versión Manual

Script para registrar coordenadas manualmente de ciudades predefinidas.

**Características:**
- ✅ Lista predefinida de ciudades (Bogotá, Medellín, Cali)
- ✅ Ingreso manual de latitud y longitud
- ✅ Validación de ciudad existente
- ✅ Almacenamiento en lista de diccionarios
- ✅ Opción de agregar múltiples ciudades

**Ejemplo de uso:**

    - Bogotá
    - Medellín
    - Cali
    ¿Que ciudad deseas agregarle lat y lon?: Medellín
    Ciudad seleccionada Medellín
    Ingresa la latitud: 6.2442
    Ingresa la longitud: -75.5812
    coordenadas agregadas para Medellín
    ¿Deseas ponerle lon y lat a otra ciudad? (si/no): no
    Finalizado
    
    Coordenadas registradas:
    {'nombre': 'Medellín', 'lat': '6.2442', 'lon': '-75.5812'}

### 🌐 Clim_weather_API.py - Versión Automática

Script que obtiene coordenadas automáticamente mediante API de geocodificación.

**Características:**
- ✅ Búsqueda de cualquier ciudad del mundo
- ✅ Obtención automática de coordenadas vía API
- ✅ Validación de existencia de ciudad
- ✅ Almacenamiento dinámico en lista
- ✅ Interfaz con emojis
- ✅ Búsqueda en español

**Ejemplo de uso:**

    🌍 Ingrese el nombre de la ciudad: París
    Coordenadas registradas:
    {'Ciudad': 'Paris', 'Latitud': 48.8534, 'Longitud': 2.3488}
    ¿Deseas intentar con otra ciudad? (si/no): si
    
    🌍 Ingrese el nombre de la ciudad: Tokio
    Coordenadas registradas:
    {'Ciudad': 'Paris', 'Latitud': 48.8534, 'Longitud': 2.3488}
    {'Ciudad': 'Tokyo', 'Latitud': 35.6895, 'Longitud': 139.6917}
    ¿Deseas intentar con otra ciudad? (si/no): no
    Cerrando programa

## 🔧 Funciones Principales

### Versión Manual

#### obtener_coordenadas()

Solicita al usuario que seleccione una ciudad y agregue coordenadas manualmente.

    def obtener_coordenadas():
        while True:
            for ciudad in ciudades:
                print("-", ciudad)
            
            c = input("¿Que ciudad deseas agregarle lat y lon?: ").strip()
            if c in ciudades:
                lat = input("Ingresa la latitud: ")
                lon = input("Ingresa la longitud: ")
                coordenadas_ciudades.append({"nombre": c, "lat": lat, "lon": lon})

**Validaciones:**
- ✅ Verifica que la ciudad esté en la lista predefinida
- ✅ Manejo de excepciones para valores no válidos
- ✅ Opción de salida del bucle

### Versión API

#### obtener_coordenadas(ciudad)

Obtiene coordenadas automáticamente desde la API de Open-Meteo.

    def obtener_coordenadas(ciudad):
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        parametros = {"name": ciudad, "count": 1, "language": "es"}
        resp = requests.get(geo_url, params=parametros)
        data = resp.json()
        
        if resp.status_code == 200 and data.get("results"):
            datos = resp.json()["results"][0]
            return datos["latitude"], datos["longitude"], datos["name"]
        return None, None, None

**Parámetros:**
- `ciudad` (str): Nombre de la ciudad a buscar

**Retorna:**
- `tuple`: (latitud, longitud, nombre_oficial) o (None, None, None)

## 📊 Comparación de Versiones

| Característica          | Manual           | API              |
|-------------------------|------------------|------------------|
| Ciudades disponibles    | 3 predefinidas   | Cualquier ciudad |
| Ingreso de datos        | Manual           | Automático       |
| Precisión               | Depende usuario  | Alta             |
| Requiere internet       | No               | Sí               |
| Validación              | Lista fija       | API real         |
| Dificultad              | Básica           | Intermedia       |

## 🌐 API Utilizada (Versión API)

**Open-Meteo Geocoding API**

- **Endpoint:** `https://geocoding-api.open-meteo.com/v1/search`
- **Método:** GET
- **Parámetros:**
  - `name`: Nombre de la ciudad
  - `count`: Número de resultados (1)
  - `language`: Idioma de búsqueda (es)

## 💾 Estructura de Datos

Ambas versiones almacenan las coordenadas en una lista de diccionarios:

### Versión Manual:

    [
        {"nombre": "Medellín", "lat": "6.2442", "lon": "-75.5812"},
        {"nombre": "Bogotá", "lat": "4.7110", "lon": "-74.0721"}
    ]

### Versión API:

    [
        {"Ciudad": "Paris", "Latitud": 48.8534, "Longitud": 2.3488},
        {"Ciudad": "Tokyo", "Latitud": 35.6895, "Longitud": 139.6917}
    ]

## 🎯 Casos de Uso

### Versión Manual
- 📚 Proyectos educativos básicos
- 🔧 Prototipado rápido sin internet
- 📝 Aprendizaje de estructuras de datos
- 🎓 Práctica de bucles y validaciones

### Versión API
- 🌍 Aplicaciones con datos reales
- 🗺️ Sistemas de mapeo
- 📍 Geolocalización dinámica
- 🚀 Proyectos escalables

## 🚀 Mejoras Futuras

- [ ] Persistencia de datos en archivo JSON
- [ ] Validación de formato de coordenadas (rango válido)
- [ ] Integración de ambas versiones en un solo script
- [ ] Interfaz gráfica con tkinter
- [ ] Exportación a CSV/Excel
- [ ] Visualización en mapa interactivo
- [ ] Cálculo de distancias entre ciudades
- [ ] Búsqueda por país o región
- [ ] Sistema de favoritos
- [ ] Historial de búsquedas

## 🎓 Conceptos Aplicados

### Versión Manual
- **Listas y Diccionarios**: Estructuras de datos básicas
- **Bucles while**: Control de flujo
- **Input/Output**: Interacción con usuario
- **Validaciones**: Verificación de datos
- **Manejo de excepciones**: try/except

### Versión API
- **Consumo de APIs REST**: Peticiones HTTP
- **Procesamiento JSON**: Manejo de respuestas
- **Validación de respuestas**: Códigos de estado
- **Estructuras dinámicas**: Listas variables
- **Geocodificación**: Conversión nombre a coordenadas

## 📖 Ejemplo Completo

### Flujo Manual:

    Inicio
      ↓
    Mostrar lista de ciudades predefinidas
      ↓
    Usuario selecciona ciudad
      ↓
    Usuario ingresa lat/lon manualmente
      ↓
    Guardar en lista de diccionarios
      ↓
    ¿Agregar otra? → Si: repetir | No: finalizar
      ↓
    Mostrar todas las coordenadas registradas

### Flujo API:

    Inicio
      ↓
    Usuario ingresa nombre de ciudad
      ↓
    Consultar API de Open-Meteo
      ↓
    ¿Ciudad encontrada?
      Sí → Obtener lat/lon/nombre
      No → Solicitar otra ciudad
      ↓
    Guardar en lista de diccionarios
      ↓
    ¿Buscar otra? → Si: repetir | No: finalizar
      ↓
    Mostrar todas las coordenadas registradas

## 🌍 Ciudades de Ejemplo

### Versión Manual (Predefinidas):
- 🇨🇴 Bogotá (4.7110, -74.0721)
- 🇨🇴 Medellín (6.2442, -75.5812)
- 🇨🇴 Cali (3.4516, -76.5320)

### Versión API (Cualquier ciudad):
- 🇫🇷 París
- 🇯🇵 Tokio
- 🇺🇸 Nueva York
- 🇪🇸 Madrid
- 🇧🇷 São Paulo
- 🇬🇧 Londres

## 💻 Requisitos del Sistema

### Versión Manual:
- Python 3.x

### Versión API:
- Python 3.x
- Librería requests
- Conexión a Internet

## 👨‍💻 Información del Desarrollador

**Nombre:** SebitasDown  
**GitHub:** @SebitasDown  
**Proyecto:** Clim Weather - Coordinate Management System

## 📄 Licencia

Proyecto educativo - Código abierto para aprendizaje

---

**Desarrollado con 💙 Python y 🌍 pasión por la geografía**
