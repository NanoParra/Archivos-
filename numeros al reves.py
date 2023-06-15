num1=int(input("Ingrese un numero: \n"))
a=1
resultado=0
while a <=3:
    resto=num1%10
    resultado=(resultado*10)+resto
    num1=num1//10
    a+=1
    print("El resultado es: ",resultado)


    '''
    prueba
    va a tener 2 menu 

    login 

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
    ''' 