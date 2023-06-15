                                                        #FUNCION PARA AGRUPAR INFORMACION Y MOSTRARLA



def sumar_dos_numeros():                        #funcion sin parametros y sin retorno 
    print("Sumando dos numeros")
    num1=6 #(int(input("Ingrese el primero numero")))
    num2=10 #(int(input("Ingrese el segundo numero")))
    resultado=num1*num2
    print(f"el resultado de la suma es {resultado}")
sumar_dos_numeros()

                                            #funcion sin parametros y con retorno
def sumar_dos_numeros_retorno2():
    print("Sumando dos numeros")
    num1=6
    num2=10
    resultado=num1*num2
    return resultado
resultado=sumar_dos_numeros_retorno2()+20
print(f"el resultado de la suma es {resultado}")


                                            #funcion con parametros sin retorno
def sumar_dos_numeros3(num1,num2):
    print("Sumando dos numeros")
    resultado=num1*num2
    print(f"el resultado de la suma es {resultado}")
sumar_dos_numeros3(333,444)

                                    #FUNCION QUEAGRUPA TODO TIPO DE INFORMACION CON EL CODICO (*args)

def varios_valores(*args):
    for arg in args:
        print(arg)
varios_valores("hola como estas", 123,777)

