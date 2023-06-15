usuario1="fcalfun"
contraseña1="1234"
usuario2="sebastian"
contraseña2="2312"
cantidad="error"
total=0
opcion=0
descuento="error"
jornada="error"
opcionmenu="error"
contadortradicional=0
contadorpepperoni=0
valordescuento=0
contadorallmeat=0
flaglogin=False
while flaglogin==False :
    print("Bienvenido al la pizzeria ''Pizzaduoc''\n Para poder entrar al menu por favor inicie sesion")
    usuario=str(input("Ingrese su usuario\n")).lower() #El lower es para que las letras que pongas se hagan minisculas
    try:
        contraseña=int(input("Ingrese su contraseña"))
    except ValueError:
        print("La contraseña son solo numeros")
    if usuario==usuario1 and contraseña==contraseña1 or usuario==usuario2 and contraseña==contraseña2:
        flaglogin=True
    else:
        print("Ingreso mal sus datos por favor reintente")


while flaglogin==True:
    try:
        opcionmenu=int(input("Que desea hacer: \n (1) Ver menu RAPID\n (2) Pagar\n (3) Anular pedido \n (4) Salir del programa"))
    except ValueError:
         print("Por favor solo ingrese numeros")
    if opcionmenu==1:
        while opcion!=4:
            try:
                opcion=int(input("------------------Menu RAPID-----------------\n Que desea comprar\n (1) Pizza Tradicional $12000\n (2) Pizza peperoni $14000\n (3) Pizza todo carnes $17000\n (4) Volver al menu anterior"))
            except ValueError:
                print("Por favor solo ingrese numeros")
                opcion="error"
            if opcion==1:
                while cantidad=="error":
                    try:
                        cantidad=int(input("¿Cuantas pizza tradicionales desea llevar?"))
                    except ValueError:
                        print("Por favor solo ingrese numeros")
                    valor=cantidad*12000
                    try:
                        total=total+valor
                        contadortradicional=contadortradicional+cantidad
                    except TypeError:
                        ""
                    opcion=0
            elif opcion==2:
                while cantidad=="error":
                    try:
                        cantidad=int(input("¿Cuantas pizza pepperoni desea llevar?"))
                    except ValueError:
                        print("Por favor solo ingrese numeros")
                    valor=cantidad*14000
                    try:
                        total=total+valor
                        contadorpepperoni=contadorpepperoni+cantidad
                    except TypeError:
                        ""
                    opcion=0
            elif opcion==3:
                while cantidad=="error":
                    try:
                        cantidad=int(input("¿Cuantas pizza todo carne desea llevar?"))
                    except ValueError:
                        print("Por favor solo ingrese numeros")
                    valor=cantidad*17000
                    try:
                        total=total+valor
                        contadorallmeat=contadorallmeat+cantidad
                    except TypeError:
                        ""
                    opcion=0
            elif opcion==4:
                    ""
            elif opcion=="error":
                ""
                opcion=0
            else:
                print("Ingrese una opcion valida")
            cantidad="error"
    elif opcionmenu==2:
        while descuento=="error":
            try:
                descuento=int(input("¿Usted tiene descuento?\n (1) Si \n (2) No"))
            except ValueError:
                print("Al no poner un numero no tiene acceso al descuento")
                descuento="error"
            if descuento==1:
                while jornada=="error":
                    try:
                        jornada=int(input("¿Que tipo de jornada tiene?\n (1) Diurna\n (2) Vespertina\n (3)Administrativa"))
                    except ValueError:
                        print("Por favor ingrese un numero")
                    if jornada==1:
                        valordescuento=0.12
                    elif jornada==2:
                        valordescuento=0.1
                    elif jornada==3:
                        valordescuento=0
                    elif jornada=="error":
                        ""
                    else:
                        print("Por favor ingrese un valor dentro de los rangos mostrados")
            elif descuento=="error":
                ""
            elif descuento==2:
                print("No tiene descuento")
            else:
                print("No ingreso un valor dentro los otorgados")
                descuento="error"
        print("PizzasDuoc\n\n----------------------------------------------------------------------------------")
        if contadortradicional!=0:
            print(f" {contadortradicional} Pizza Tradicional $ {contadortradicional*12000}")
        if contadorpepperoni!=0:
            print(f" {contadorpepperoni} Pizza Pepperoni $ {contadorpepperoni*14000}")
        if contadorallmeat!=0:
            print(f" {contadorallmeat} Pizza Todo Carne $ {contadorallmeat*17000}")
        print(f"----------------------------------------------------------------------------------\n Subtotal                                                         $ {total}\n Descuento {valordescuento*100}%                                                  $  {total*valordescuento}\n----------------------------------------------------------------------------------\n Total a pagar                                                      $ {total*(1-valordescuento)}\n\n\n Gracias por su Compra!")
        flaglogin=False
    elif opcionmenu==3:
        print("Usted acaba de anular su pedido")
        total=0
        opcionmenu=="error"                
    elif opcionmenu==4:
        print("Muchas gracias por ocupar el programa")
        flaglogin=False
    elif opcionmenu=="error":
        ""
    else:
        print("Por favor ingrese una opcion dentro del rango asignado")               


                    
                