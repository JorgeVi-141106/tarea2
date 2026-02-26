import subprocess
subprocess.run("cls", shell=True)

def asignar_repartidor(zona_pedido, **kwargs):
    for nombre, datos in kwargs.items():
        if datos["disponible"] and datos["zona"] == zona_pedido:
            datos["disponible"] = False
            return nombre.capitalize()
    return None


# Repartidores (2 por zona)
repartidores = {
    "juan": {"disponible": True, "zona": "marbella"},
    "pedro": {"disponible": True, "zona": "marbella"},
    
    "ana": {"disponible": True, "zona": "torices"},
    "laura": {"disponible": True, "zona": "torices"},
    
    "carlos": {"disponible": True, "zona": "bicentenario"},
    "sofia": {"disponible": True, "zona": "bicentenario"}
}


# Ingresar cantidad de pedidos
cantidad = int(input("¿Cuántos pedidos deseas asignar? "))

for i in range(1, cantidad + 1):
    zona = input(f"Ingrese la zona del pedido #{i}: ").strip().lower()
    
    asignado = asignar_repartidor(zona, **repartidores)
    
    if asignado:
        print(f"Pedido #{i}: Repartidor asignado → {asignado}")
    else:
        print(f"Pedido #{i}: No hay repartidores disponibles en {zona}")


print("\n--- Estado final de repartidores ---")
for nombre, datos in repartidores.items():
    estado = "Disponible" if datos["disponible"] else "Ocupado"
    print(f"{nombre.capitalize()} ({datos['zona']}): {estado}")