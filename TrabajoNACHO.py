import random

def generar_sorteo():
    numeros_totales = list(range(1, 50));
    sorteo = random.sample(numeros_totales, 7);
    return sorteo;
numeros_jugador = [];
for i in range(1,6):
    numero = int(input(f"{i}.- Ingresa un número entre 1 y 49: "));
    try:
        if numero < 1 or numero > 49:
            print ("Ingresa un numero valido");
    except ValueError:
        print ("Ingresa un numero valido");
    numeros_jugador.append(numero);
sorteo = generar_sorteo();
print ("------------------------------------");
print ("Los números sorteados en la ronda 1 son :");
print("\nNúmeros del sorteo:", sorteo);
print ("--------------------------------------");
if (numeros_jugador)==(sorteo):
    print("¡Wena ganaste la ronda!");
else:
    print("Perdiste la ronda .-. no acertaste una ");
print ("---------------------------------------");