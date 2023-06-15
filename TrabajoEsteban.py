import random
lista_datos=[]
numeros_ruleta=[]
numeros_ruleta=random.sample(range(1, 50), 5)
print("-------------------Ruleta-------------------\n")
print("---------Ingrese un numero del 1 al 49------------\n")
for i in range(5):
    while True:
        try:
            numero = int (input("Ingresa el número: "))
            if numero>0 and numero<=49:
                    print("El numero ingresado es: ",numero)
            else:
                    print("'''El numero ingresado no es valido, intente nuevamente'''")
            lista_datos.append(numero)
            break
        except ValueError:
            print("'''ingrese numeros, intente de nuevo'''")
print(f"Usted ingreso los siguentes números: {lista_datos}")
for x in range(0,5):
    print(f"Los numeros ganadores son: {random.choices(numeros_ruleta)}\n")
if lista_datos==numeros_ruleta:
    print(f"Usted a ganados la ruleta con los siguentes numeros: {numeros_ruleta}")
else:
     print("'''Usted no gano nada'''")
    

print("-------------------Fin Ruleta-------------------\n")

