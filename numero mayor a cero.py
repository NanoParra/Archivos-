contarvocales=0;
contarConsonantes=0;
for i in range(10):
    letra=input("Ingrese una letra: \n");
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        contarvocales+=1;
else:
    contarConsonantes+=1
print("El numero de vocales es: "+str(contarvocales));
print("El numero de consonantes es: "+str(contarConsonantes));


