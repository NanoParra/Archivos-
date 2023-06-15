'''crear  menu, con 3 opciones
iniciar secion 
cambiar contraseña 
cerrar secion 
Crear login
contraseña 
permitir 3 intentos 
o se bloqueael usuario
'''
flag=True

user1="admin"
password1="admin"
password3=str
i=0

print("---------------Menu--------------")
print("1.-Iniciar seción")
print("2.-Cambiar contraseña ")
print("3.-Cerrar sesión ")
while i<3:
    opcion=input("Ingrese la opción deseada: ")
    if opcion=="1":
        print("'INGRESE SU USUARIO Y PASSWORD'")
        user=input("Usuario: ")
        password=input("Password: ")
    if (user==user1)and(password==password1):
        print("Acceso concedido")
        print(" ")
    else:
        print("Acceso denegado")
        print(" ")
        print("Error en la cuenta igresada")
        print(" ")
    i+=1
    if i==3:
         print ("Has sobrepasado el numero de intentos")


    if opcion=="2":
        print("'INGRESE SU CONTRASEÑA NUEVA'")
        password1= input("Contraseña: ")
    elif password3==password1:
        print("Contraseña cambiada")
        print(" ")
    
    
    if opcion=="3":
        print("'CERRANDO SESIÓN'")
        break

    
