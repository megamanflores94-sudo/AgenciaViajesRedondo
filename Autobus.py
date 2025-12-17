def agencia_viajes():
    print("AGENCIA DE VIAJES EN AUTOBÚS")
    print("1. Acapulco - $850")
    print("2. Michoacán - $700")

    opcion = int(input("Elige el destino (1 o 2): "))
    pasajeros = int(input("Ingresa el número de pasajeros: "))

    if opcion == 1:
        destino = "Acapulco"
        costo = 850
    elif opcion == 2:
        destino = "Michoacán"
        costo = 700
    else:
        print("Opción no válida")
        return

    total = pasajeros * costo

    print("\nRESUMEN DEL VIAJE")
    print("Destino:", destino)
    print("Pasajeros:", pasajeros)
    print("Costo por pasajero: $", costo)
    print("Total a pagar: $", total)

# Ejecutar el programa
agencia_viajes()