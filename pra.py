import os
os.system('cls')

def registro_pedido(cliente="Consumidor Final", descuento=0, **productos):
    total = 0
   
    print("----- PEDIDO -----")
    print("Cliente:", cliente)
    print("------------------")

    for nombre, datos in productos.items():
        direccion, telefono, cantidad, precio = datos
        subtotal = cantidad * precio
        total += subtotal

        
        print(f"direccion: {direccion}")
        print(f"telefono: {telefono}")
        print(f"Artículo: {nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio unitario: ${precio}")
        print(f"Subtotal: ${subtotal}")
        print("------------------")

    total_final = total - descuento
    
    print("Subtotal:", total)
    print("Descuento:", descuento)
    print("TOTAL A PAGAR:", total_final)

registro_pedido(
    cliente="Carlos",
    descuento=10,
    arroz=("bicentenario","12783012",2, 20),
    
)
