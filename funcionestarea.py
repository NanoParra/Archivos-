def mostrar_menu():
    print("\t---------------MNEU---------------")
    print("1.- Calcula IVA")
    print("2.- Calcular DESCUENTO")
    print("3.- Calcula IMC")
    print("4.- Salir")
def calcular_iva(totalcompra):
    resultado = totalcompra * 0.19
    print(f"El IVA es de:  {resultado}")

def calcular_descunto(totalcompra):
    descuento= totalcompra * 0.3
    resultado=totalcompra-descuento
    print("\n-----------BOLETA-----------")

