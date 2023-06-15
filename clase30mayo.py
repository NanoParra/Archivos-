import numpy as np
arreglo = np.random.randint(0, 101, size=10)
print(arreglo)


def analizar_arreglo(arreglo):
    
    copia_arreglo = arreglo.copy()
    print("Copia del arreglo:", copia_arreglo)
    elemento_mayor = max(copia_arreglo)
    print("Elemento mayor:", elemento_mayor)
    elemento_menor = min(copia_arreglo)
    print("Elemento menor:", elemento_menor)
    suma_elementos = sum(copia_arreglo)
    print("Suma de los elementos:", suma_elementos)
    promedio_elementos = suma_elementos / len(copia_arreglo)
    print("Promedio de los elementos:", promedio_elementos)
    print("Todos los elementos:")
    for elemento in copia_arreglo:
        print(elemento)
arreglo = [5, 10, 2, 8, 3]
analizar_arreglo(arreglo)
