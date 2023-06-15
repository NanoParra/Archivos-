contador=0
flag=False
acumulador=0
print("Ingrese un numero")
num1=int(input())
print("Ingrese un numero")
num2=int(input())
print("Ingrese un numero")
num3=int(input())
if num1%2==0:
    acumulador=acumulador+num1
    contador=contador+1
    flag=True
if num2%2==0:
        acumulador=acumulador+num2
        contador=contador+1
        flag=True
if num3%2==0:
    acumulador=acumulador+num3
    contador=contador+1
    flag=True
else :
    print(f"El total de numero es: {acumulador}")
    print(f"El total de numero es: {contador}")
    print(f"El el numero es: {flag}")
    
    
    