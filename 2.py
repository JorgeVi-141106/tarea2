import subprocess
subprocess.run("cls", shell=True)

def calcular_totales(info_ruta):
    distancia_total = info_ruta["distancia"] * 2
    precio_total = info_ruta["precio"] * 2
    return {
        "distancia_total": distancia_total,
        "precio_total": precio_total
    }


def motor_rutas(**kwargs):
    entrada_usuario = input("Escribe los destinos (separados por coma): ")
    destinos = [x.strip().lower() for x in entrada_usuario.split(",")]

    resultados = []

    for nombre_ruta, datos in kwargs.items():
        if nombre_ruta in destinos:
            totales = calcular_totales(datos)

            resultados.append({
                "destino": nombre_ruta,
                "distancia_total": totales["distancia_total"],
                "precio_total": totales["precio_total"]
            })

    return resultados


def evaluar(resultados):
    if not resultados:
        return None, None

    mejor_precio = resultados[0]
    mejor_distancia = resultados[0]

    for elemento in resultados:
        if elemento["precio_total"] < mejor_precio["precio_total"]:
            mejor_precio = elemento

        if elemento["distancia_total"] < mejor_distancia["distancia_total"]:
            mejor_distancia = elemento

    return mejor_precio, mejor_distancia


# Datos fijos
pedidos = motor_rutas(
    marbella={"distancia": 10, "precio": 10000},
    torices={"distancia": 15, "precio": 25000},
    bicentenario={"distancia": 30, "precio": 70000}
)


for pedido in pedidos:
    print("\nDestino:", pedido["destino"].capitalize())
    print("Distancia total:", pedido["distancia_total"], "km")
    print("Precio total: $", pedido["precio_total"])


barata, rapida = evaluar(pedidos)

if barata and rapida:
    print("\nRuta más económica:", barata["destino"].capitalize())
    print("Ruta más rápida:", rapida["destino"].capitalize())
else:
    print("\nNo ingresaste rutas válidas.")