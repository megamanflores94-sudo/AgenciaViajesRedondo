#Luis Angel Limon Hernandez 
#programa de avion redondo 
def agencia_viajes():
    print("AGENCIA DE VIAJES EN AVION")
    print("1. Acapulco - $500")
    print("2. Michoacán - $1000")

    opcion = int(input("Elige el destino (1 o 2): "))
    pasajeros = int(input("Ingresa el número de pasajeros: "))

    if opcion == 1:
        destino = "Acapulco"
        costo = 500
    elif opcion == 2:
        destino = "Michoacán"
        costo = 1000
    else:
        print("Opción no válida")
        return

    total = pasajeros * costo

    print("\nRESUMEN DEL VIAJE")
    print("Destino:", destino)
    print("Pasajeros:", pasajeros)
    print("Costo por pasajero: $", costo)
    print("Total a pagar: $", total)