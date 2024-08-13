import json

contador=1
totalPagar=23

with open("pedidos.json","r")as a:
    pedidoJson= json.load(a)

with open("menu.json","r")as a:
    menujson= json.load(a)

with open("pagos.json","r")as a:
    pagosjson= json.load(a)

print("MoliPollito")
print("")
print("1. Registras Compra")
opcion=int(input(""))

if opcion==1:

    nameCliente=str(input("Ingrese su nombre: "))
    fecha=str(input("Ingrese la fecha del día de hoy: "))

    print("|Menú|")
    for i in menujson:
        
        print("----------Plato ", contador,"-----------")
        print("")
        print(f"Categoría: {i["categoria"]}")
        print(f"Nombre: {i["nombre"]}")
        print(f"Precio: {i["precio"]}")
        contador=contador+1
        print("-------------------------------")
        print("")

    opcionA=str(input("Deseas la entrada (s/n)"))
    if opcionA=="s":

        for i in menujson:

            if i["categoria"]=="entrada":

                print("----------Entrada ", contador,"-----------")
                print("")
                print(f"Id: {i["id"]}")
                print(f"Nombre: {i["nombre"]}")
                print(f"Precio: {i["precio"]}")

                contador=contador+1

                print("---------------------------------")
                print("")
        id=int(input("Ingrese el id: "))
        nombreA= str(input("Nombre: "))
        cantidadA=int(input("Cantidad: "))

        for i in menujson:
            if i["id"]==id:
                print(f"precio {i["precio"]}")

    opcionB=str(input("Deseas el platillo fuerte? (s/n)"))
    if opcionB=="s":
        id=int(input("Ingrese el id: "))
        nombreB= str(input("Nombre: "))
        cantidadB=int(input("Cantidad: "))
    
    opcionC=str(input("Deseas la bebida ? (s/n)"))
    if opcionC=="s":
        id=int(input("Ingrese el id: "))
        nombreC= str(input("Nombre: "))
        cantidadC=int(input("Cantidad: "))
    
    print("")
    print("Su orden")
    print("")
    if opcionA=="s":
        print("Id: ", id)
        print("Nombre: ", nombreA)
        print("Cantidad: ", cantidadA)
        print("Precio", )
        print("")
    if opcionB=="s":
        print("Id: ", id)
        print("Nombre: ", nombreB)
        print("Cantidad: ", cantidadB)
        print("")
    if opcionC=="s":
        print("Id: ", id)
        print("Nombre: ", nombreC)
        print("Cantidad: ", cantidadC)
        print("")
    
    confirmacion=str(input("Confirme su orden (s/n)"))

    if confirmacion=="s":

        if opcionA=="s":

            pedidoClienteA={
                "cliente": nameCliente,
                "items": [
                    {
                        "categoria": "entrada",
                        "id": id,
                        "nombre": nombreA,
                        "cantidad": cantidadA,
                        "precio": 9000
                    },
                ]
            }
            pedidoJson +=[pedidoClienteA]
        
            with open("pedidos.json", "w")as b:
                json.dump(pedidoJson, b, indent=4)

        if opcionB=="s":
            pedidoClienteB={
            "cliente": nameCliente,
                "items": [
                    {
                        "categoria": "plato_fuerte",
                        "id": id,
                        "nombre": nombreB,
                        "cantidad": cantidadB,
                        "precio": 9000
                    },
                ]
            }
            pedidoJson +=[pedidoClienteB]
        
            with open("pedidos.json", "w")as b:
                json.dump(pedidoJson, b, indent=4)

        if opcionC=="s":
            pedidoClienteC={
            "cliente": nameCliente,
                "items": [
                    {
                        "categoria": "bebidas",
                        "id": id,
                        "nombre": nombreC,
                        "cantidad": cantidadC,
                        "precio": 9000
                    },
                ]
            }
            pedidoJson +=[pedidoClienteC]
        
            with open("pedidos.json", "w")as b:
                json.dump(pedidoJson, b, indent=4)


        print("Su orden fue guardada exitosamente :)")
        
        print("|PAGO|")
        print("1. Ingesar fecha de pago")
        print("2. Pagar")

        opcionPago=int(input("Ingrese el número de la opción que deseas: "))

        if opcionPago==1:

            fechaPago=int(input("Ingrese la fecha de pago: "))

            pago={
                "cliente": nameCliente,
                "total": 47000,
                "fecha_pago": fechaPago
            }

            pagosjson +=[pago]

            with open("pagos.json","w")as b:
                json.dump(pagosjson, b, indent=4)

        if opcionPago==2:
            
            print("Pagar ahora")
            print("")
            print(f"Pago a realizar ", totalPagar)
            confirmarPago=str("Confirmar pago (s/n)")
            if confirmarPago=="s":
                print("Pago exitoso")
            if confirmarPago=="n":
                print("Pago no realizado, su pedido no será agregado")

    if confirmacion=="n":
        print("")
        print("Su orden no fue guardada")