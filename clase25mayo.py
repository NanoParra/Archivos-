'''lista_nombres=[54,67,87,24,50]
print (lista_nombres[0])
print (lista_nombres[1])
print (lista_nombres[2])
print (lista_nombres[3])
print (lista_nombres[4])
lista_nombres.append(12)
''
print (lista_nombres)

num=int(input("ingrese un numero"))
lista_nombres.append(num)
'''

'''edad 
nombre 
apellido'''


lista_datos=[]
nombre=input("inrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
lista_datos.append(nombre)
lista_datos.append(apellido)
lista_datos.append(edad)

print(lista_datos)

'''
print (f"El nombre es : {lista_datos[0]}")
print (f"El apellido es : {lista_datos[1]}")
print (f"La edad es : {lista_datos[2]}")
lista_datos.insert(2,"juanito")
print(lista_datos)
lista_datos.remove("juanito")
print (lista_datos)
lista_datos.pop()
print(lista_datos)
'''
'''

lista_multi=[]

num=int(input("ingrese un numero: "))
for i in range(1,11):
    resultado=num*i
    lista_multi.append(resultado)
    print (f"{num} x {i} = {resultado}")
print(lista_multi)
'''


num2=int(input("Ingrese otro numero: "))
        num3=int(input("Ingrese otro numero: "))
        num4=int(input("Ingrese otro numero: "))
        num5=int(input("Ingrese otro numero: "))
        num6=int(input("Ingrese otro numero: "))
        num7=int(input("Ingrese otro numero: "))
 try: 
        numeros=int(input("Ingrese un numero: "))
        if numeros>0 and numeros<=49:
            lista_datos.append(numeros)
            print("El numero ingresado es: ",numeros)
        else:
            print("El numero ingresado no es valido")
    except TypeError:
        print("Ingrese numeros, no letras")

    lista_datos.append(num1)