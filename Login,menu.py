user="admin"
password="admin"
print("---------------------Menu---------------------")
print(" ")
print("'INGRESE SU USUARIO Y PASSWORD PARA ACCEDER AL MENU'")
user1= input("Usuario: ")
password1=input("Password: ")
if (user==user1)and(password==password1):
    print("Acceso concedido")
    print(" ")
    
else:
    print("Acceso denegado")
    print(" ")
    print("Error en la cuenta igresada")
    print(" ")

def mostrar_menu():
    print("Menu de opciones:")
    print("1. Opción ")
    print("2. Opción ")
    print("3. Salir")


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        print("Seleccionó la opción 1")
    elif opcion == "2":
        print("Seleccionó la opción 2")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

        


