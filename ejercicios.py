zapatos=20.000
acumulador=1
flag=False
print("\n")
print("Por la compra sobre los 40.000, usted optiene un envio gratis")
print("Indique la cantidad de zapatos que decea comprar:\n")
resultado=int (input())

if resultado+40.000:
    acumulador=resultado+zapatos
    print(f"Usted lleva una cantidad de :{acumulador}")
    print("Usted a optenido un envio gratis")
  

else:
    print("Usted debe cancelar un monto de $3.000 por la cantidad de zapatos que lleva")

print(f"EL total de la comprar es: {acumulador}00")