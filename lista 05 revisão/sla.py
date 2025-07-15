import math

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Converter graus para radianos
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Fórmula de Haversine
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    raio_terra_km = 6371
    distancia = raio_terra_km * c
    return distancia

if __name__ == "__main__":
    print("Informe as coordenadas do primeiro lugar:")
    lat1 = float(input("Latitude 1: "))
    lon1 = float(input("Longitude 1: "))
    print("Informe as coordenadas do segundo lugar:")
    lat2 = float(input("Latitude 2: "))
    lon2 = float(input("Longitude 2: "))
    distancia = calcular_distancia(lat1, lon1, lat2, lon2)
    print(f"A distância entre os dois lugares é de {distancia:.2f} km.")