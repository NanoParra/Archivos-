'''crear  menu, con 3 opciones
iniciar secion 
cambiar contraseña 
cerrar secion 
Crear login
contraseña 
permitir 3 intentos 
o se bloqueael usuario
'''
user="admin"
paswoord="admin"
flag=True
contador=1
while contador<=3:

    print(" ")
    print(" 'Ingrese su Usuario y contraseña para acceder al menu' ")
    print(" ")
    user1=input("Ususario: ")
    paswoord1=input("Contraseña: ")
    if (user==user1) and (paswoord==paswoord1):
        print("Acceso concedido")
        print("") 
        contador=4
        while True:
            print("---------------Menu--------------")
            print("1.-Cambiar contraseña ")
            print("2.-Cerrar sesión ")
            opcion=input("Ingrese una opcion: \n")
            if opcion=="1":
                print()
                paswoord=input("Ingrese la nueva contraseña ")
            if opcion=="2":
                print("Cerrando!")
                break

    else:
        print("")
        print("Acceso denegado")
        print(" ")
        print("Error en la cuenta igresada")
        print(" ")

        contador=contador+1