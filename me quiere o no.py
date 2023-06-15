a=0
b=3
try:
    resultado= a*b
    print(resultado)
except TypeError:

    print("Error en la división")
except ZeroDivisionError:
    print("Error en la división")