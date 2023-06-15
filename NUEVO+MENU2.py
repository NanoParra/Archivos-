opciones ={1: "Pan Amasado", 2: "Pan Molde", 3: "Baguette", 4: "Pan Integral"}
orden={}
flag=True
mostrar_menu=int
print("Menu de opciones:")
print("1. Comparar Pan")
print("2. Emitir Boleta")
print("3. Salir")
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Panaderia delivery")
        print("1.Pan Amasado--------$1.500")
        print("2.Pan Molde--------$1.000")
        print("3.Baguette--------$2.000")
        print("4.Pan Integral--------$3.000")
        print("5.Salir")
        while True:
            opcion = input("Ingrese el número de la opción deseada: ")
    
            if opcion == '5':
                break
            elif opcion.isdigit() and int(opcion) in opciones:
                cantidad = input("Ingrese la cantidad: ")
                if cantidad.isdigit():
                    orden[opciones[int(opcion)]] = int(cantidad)
                else:
                    print("Cantidad inválida. Intente nuevamente.")
            else:
                print("Opción inválida. Intente nuevamente.")
            
    elif opcion == "2":
        if len(orden) > 0:
            precios = {
                "Pan Amasado": 1500,
                "Pan Molde": 1000,
                "Baguette": 2000,
                "Pan Integral": 3000
                }
            total = 0
            print("--------------- Boleta de Venta ---------------")
            print("Ítem\t\t\tCantidad\t\tPrecio\t\tSubtotal")
            print("------------------------------------------------")

        for pan, cantidad in orden.items():
            if pan in precios:
                precio_unitario = precios[pan]
                subtotal = precio_unitario * cantidad
                total += subtotal
                print(f"{pan}\n\n\n{cantidad}\n\n\n{precio_unitario}\n\n\n{subtotal}")
        print("-----------------------------------------------")
        print("Total a pagar:", total)
        if total > 5000:
            print("Envío gratis")
        else:
            recargo = total * 0.1
            print("Envío del 10%:", recargo)
            print("Total a pagar (con envío):", total + recargo)

    elif opcion == "3":
        print("Saliendo del programa...")
    break
else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
except ValueError:

