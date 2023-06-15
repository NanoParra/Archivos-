dolar=790.58
peso_argentino=3.63
peso_chileno=792.06
print("Que quieres convertir \n1-.Dolar a peso Chileno \n2-.Peso chileno a dolar \n3-.Peso argentino a peso chileno \n")
opcion=int(input())
if opcion==1:
    cantidad=float (input("¿Cuantos dolares deseas convertir a peso chileno?\n")) 
    peso_chileno=cantidad*dolar
    print(f"Los {cantidad} Dolares son igual a {peso_chileno} pesos chilenos")
elif opcion==2:
    cantidad=float(input("¿Cuantos pesos chilenos desea convertir a dolar\n?")) 
    dolar=cantidad*peso_chileno
    print(f"Los {cantidad} pesos chilenos son igual a {dolar} dolares")
elif opcion==3:
      cantidad=float(input("¿Cuantos pesos argentinos desea convertir a pesos chilenos?\n")) 
      peso_argentino=cantidad*peso_chileno
      print(f"Los {cantidad} pesos argentinos son igual a {peso_chileno} pesos chilenos ")
       
       

   
