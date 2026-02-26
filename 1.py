import subprocess
subprocess.run("cls", shell=True)

def registro_pedido(cliente="Consumidor Final", descuento=0, **productos):
    total = 0

    cliente = input("cliente: ")
    direccion = input("direccion: ")
    telefono =input("telefono: ")

    c_productos = int(input("cuantos productos va a ingresar: "))
    
    for i in range(c_productos):
        print(f"\nProducto {i+1}")
        nombre=input("Articulo: ")
        cantidad = int(input("cantidad de articulos: "))
        precio = int(input("precio del articulo: "))

        subtotal = cantidad * precio
        total += subtotal

        print("---------------")
        print("Artículo:", nombre)
        print("Cantidad:", cantidad)
        print("Precio unitario: $", precio)
        print("Subtotal: $", subtotal)
        print("---------------")
    
    descuento = float(input("\nDescuento: "))

    total_final = total - descuento

    print("\n===== FACTURA =====")
    print("Cliente:", cliente)
    print("Dirección:", direccion)
    print("Teléfono:", telefono)
    print("Subtotal:", total)
    print("Descuento:", descuento)
    print("TOTAL A PAGAR:", total_final)

registro_pedido()

