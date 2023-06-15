print("Sistema dibujando un cuadrado\n");
lado=int(input("ingrese el lado del cuadrado: "));
print(f"El lado del cuadrado es: {lado}");
for n in range(lado):
    for i in range(lado):
        print("*",end="");
print("");
