def calcular_ida_vuelta(distancia):
    return distancia * 2

def calcular_tarifa(destino, **kwargs):
    
    if destino not in kwargs:
        return "Destino no válido."
    
    distancia_base = kwargs[destino]["distancia"]
    
    distancia_total = calcular_ida_vuelta(distancia_base)
    
    precio_por_km = 2000
    total = distancia_total * precio_por_km
    
    return total

rutas = {
    "marbella": {"distancia": 10},
    "torices": {"distancia": 15},
    "bicentenario": {"distancia": 30}
}

destino_usuario = input("Ingrese destino: ").strip().lower()

resultado = calcular_tarifa(destino_usuario, **rutas)

print("Tarifa total (ida y vuelta):", resultado)